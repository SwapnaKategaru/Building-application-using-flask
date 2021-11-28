# Created virtual environment for web app using the command -> (python -m venv virtual)

# render_template - for accesses HTML pages, stores in python files and displays html of requested url 
from flask import Flask, render_template

page = Flask(__name__)                          # instantiating Flask object

@page.route('/')                                # @page - decorator and output from home() function will be mapped to this url
def home():
    return render_template("home.html")         # render_template method - renders specific html file

@page.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":                      
    page.run(debug=True)