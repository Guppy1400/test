from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def front_page():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return render_template("about.html")
