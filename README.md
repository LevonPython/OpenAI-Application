# OpenAI API Application 
This GitHub project is a web application built on the Flask framework and utilizes a PostgreSQL database. The website provides essential functionalities for creating and deleting user accounts, incorporating all the necessary minimal requirements.

## Web site structure 
In addition to the core functionalities, the project includes the following chapters:
- comprehensive documentation 
   <img src="/static/readme_screenshots/Documentation%20page%20Screenshot.png">
- an overview of the application
  <img src="/static/readme_screenshots/Main%20Page%20Screenshot.png">
- examples
  <img src="/static/readme_screenshots/Examples%20page%20Screenshot.png"> 
Notably, the example section showcases the integration of various OpenAI features using the ChatGPT API.
- "About" section.
  <img src="/static/readme_screenshots/About%20page%20Screenshot.png">

## Features
The OpenAI-powered features demonstrate the capabilities of the application, such as:
- generating pet names
  <img src="/static/readme_screenshots/Examples-%20Pet%20name%20page%20Screenshot.png" height="500" width="500">
- answering questions
  <img src="/static/readme_screenshots/Examples%20-%20q%20and%20a%20page%20Screenshot.png" height="500" width="500">
- summarizing sentences
  <img src="/static/readme_screenshots/Examples%20-%20Summarize%20name%20page%20Screenshot.png" height="500" width="500">
- dynamically generating pictures based on text input
  <img src="/static/readme_screenshots/Examples%20-%20image%20generate%20page%20Screenshot.png" height="500" width="500">
  <img src="/static/readme_screenshots/Examples%20-%20image%20generate%20create%20image%20page%20Screenshot.png" height="500" width="500">
  These features leverage the powerful language model provided by OpenAI to enhance the user experience and add an innovative touch to the website.

By combining Flask, PostgreSQL, and the OpenAI ChatGPT API, this project provides a robust foundation for building web applications with user account management capabilities. 
  <img src="/static/readme_screenshots/Login%20Page%20Screenshot.png" height="500" width="500">
  <img src="/static/readme_screenshots/Profile%20Page%20Screenshot.png">
The inclusion of extensive documentation ensures that developers can easily understand and extend the functionality of the application.



# OpenAI API Quickstart 

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd OpenAI-Application
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Before Running the app, you should run the POSTRE_SQL database server.
 To do this go to POSTGRE_REDAME.md file and execute 1, 2 steps.

9. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
