import os
import openai
from flask import Flask, redirect, render_template, request, url_for, flash
from fileinput import filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
app.secret_key = 'super secret key'

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="openaidatabase",
    user="levonyeghiazaryan"
    #password="admin"
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

def User():
    create_query = """CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    password VARCHAR(120) NOT NULL
);"""
    cur.execute(create_query)
    conn.commit()
    print(f"Table users was succussfully created")

def check_table_exists():
    cur.execute("select * from information_schema.tables where table_name=%s", ('users',))
    return bool(cur.rowcount)

def check_user_exists(username):
    cur.execute("SELECT * FROM users WHERE username=%s", (username, ))
    return bool(cur.rowcount)

def add_user(username, password):
    add_query = "INSERT INTO users(username, password) VALUES(%s, %s)"
    cur.execute(add_query, (username, generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)))
    conn.commit()

def delete_user(username):
    add_query = "DELETE FROM users WHERE username=%s"
    cur.execute(add_query, (username, ))
    conn.commit()

def check_user_data(username, password):
    print("username: ", username, " password: ", password)
    query = "SELECT password FROM users WHERE username=%s LIMIT 1"
    cur.execute(query, (username, ))
    result = cur.fetchone()
    if result is not None:
        stored_hashed_password = result[0]
        if(check_password_hash(stored_hashed_password, password)):
            return "Password is correct!"
        else:
            return "Password is incorrect."
    else:
        return "User not found."

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        pass
    username = request.args.get("username")
    if username is None:
        username = ''
    return render_template("main.html", username=username)

@app.route('/examples', methods=["GET", "POST"])
def examples():
    username = request.args.get("username")
    if username is None:
        username = ''
    return render_template("examples.html", username=username)

@app.route('/about', methods=["GET", "POST"])
def about():
    username = request.args.get("username")
    if username is None:
        username = ''
    return render_template("about.html", username=username)

@app.route('/docs', methods=["GET", "POST"])
def docs():
    username = request.args.get("username")
    if username is None:
        username = ''
    return render_template("docs.html", username=username)

@app.route('/profile', methods=["GET", "POST"])
def profile():
    username = request.args.get("username")
    usernametobedeleted = request.args.get("usernametobedeleted")
    print("username: ", username)
    if username is None:
        username = ''
    elif username == 'deleted':
        if check_user_exists(usernametobedeleted):
            delete_user(usernametobedeleted)
            flash(f"User was succesfully deleted")
            return redirect(url_for('profile'))
        else:
            flash(f"User was already deleted!")
            return redirect(url_for('profile'))
    return render_template("profile.html", username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #if current_user.is_authenticated:
    #    return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']
        #remember = True if request.form.get('remember') else False

        #user = User.query.filter_by(username=username).first()
        #print("check_user_data: ", check_user_data(username, password))
        data_status = check_user_data(username, password)
        if data_status != "Password is correct!":
            flash("Please check your login details and try again")
            flash(data_status)
            return redirect(url_for('login'))
        #if not user or not check_password_hash(user.password, password):
        #    flash('Please check your login details and try again.')
        #    return redirect(url_for('login'))

        #login_user(user, remember=remember)
        return redirect(url_for('main', username=username))

    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #if current_user.is_authenticated:
    #    username = request.form['username']
    #    return redirect(url_for('main', username=username))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']
        print(f"username: {username}, password: {password}")
        if not check_table_exists():
            User()
        if check_user_exists(username):
            flash('Username already exists.')
            return redirect(url_for('signup'))
        add_user(username, password)
        flash(f"User: {username} was successfully created")
        flash('Now please login')
        return redirect(url_for('login', username=username))
    else:
        print("GET method")
    return render_template("signup.html")

@app.route("/animal", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

@app.route("/qa", methods=("GET", "POST"))
def qa():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt = f"Q: {question}?\nA:",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"])
        return redirect(url_for("qa", question=question, result=response.choices[0].text))
    question = request.args.get("question")
    result = request.args.get("result")
    return render_template("qa.html", question=question, result=result)

def generate_answer(question):
    return """
       {} """.format(
        question.capitalize()
    )

@app.route("/summarize", methods=("GET", "POST"))
def summarize():
    if request.method == "POST":
        text = request.form["prompt"]
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Summarize this for a second-grade student:\n{text}\n",
        temperature=0.7,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0)
        return redirect(url_for("summarize", prompt=text, result=response.choices[0].text))
    prompt = request.args.get("prompt")
    result = request.args.get("result")
    return render_template("summarize.html", prompt=prompt, result=result)

@app.route("/img_intro", methods=("GET", "POST"))
def img_intro():
    return render_template("img_intro.html")

@app.route("/img", methods=("GET", "POST"))
def img_generator():
    if request.method == "POST":
        text = request.form["prompt"]
        response = openai.Image.create(
        prompt=text,
        n=1,
        size="512x512")
        image_url = response['data'][0]['url']
        return redirect(url_for("img_generator", prompt=text, result=image_url))
    prompt = request.args.get("prompt")
    result = request.args.get("result")
    return render_template("img_generator.html", prompt=prompt, result=result)

@app.route("/img_edit", methods=("GET", "POST"))
def img_edit():
    if request.method == "POST":
        cur_path =  os.getcwd()
        text = request.form["prompt"]
        response = openai.Image.create_edit(
        image=open(cur_path+"/static/img_flamingo.png", "rb"),
        mask=open(cur_path+"/static/img_flamingo_mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo",
        n=1,
        size="256x256")
        image_url = response['data'][0]['url']
        return redirect(url_for("img_edit", prompt=text, result=image_url))
    prompt = request.args.get("prompt")
    result = request.args.get("result")
    return render_template("img_editor.html", prompt=prompt, result=result)

@app.route("/img_var", methods=("GET", "POST"))
def img_variation():
    if request.method == "POST":
        f = request.files['file']
        print("FILE: ", f.filename)
        f.save(os.getcwd()+f.filename)
        cur_path =  os.getcwd()
        response = openai.Image.create_variation(
        image=open(f"{cur_path}/static/{f.filename}", "rb"),
        n=1,
        size="256x256")
        image_url = response['data'][0]['url']
        return redirect(url_for("img_variation", result=image_url))
    prompt = request.args.get("prompt")
    result = request.args.get("result")
    return render_template("img_variation.html", result=result)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

with app.test_request_context('/qa', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/qa'
    assert request.method == 'POST'
    print(url_for('qa', result='AAAAAAAAAAAA'))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=int(os.environ.get("PORT", 5050)),debug=True)
    cur.close()
    conn.close()
