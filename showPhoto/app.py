# Written by Henry Cussatt
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
	return render_template("show.html")


