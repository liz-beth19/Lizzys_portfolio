 
from flask import redirect, render_template,Flask,request

app = Flask (__name__)

@app.route('/')
def index():
    return render_template("homepage.html")


@app.route("/submit", methods=["GET","POST"])
def submit():
    return render_template("contact.html") 