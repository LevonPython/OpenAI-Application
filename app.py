import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from fileinput import filename

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/examples')
def examples():
    return render_template("examples.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/docs')
def docs():
    return render_template("docs.html")

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

with app.test_request_context('/qa', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/qa'
    assert request.method == 'POST'
    print(url_for('qa', result='AAAAAAAAAAAA'))
