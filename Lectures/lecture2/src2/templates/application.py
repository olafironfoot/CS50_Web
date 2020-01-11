from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline="woah headline! now?"
    return render_template("index.html", headline=headline)

@app.route("/Bye")
def bye():
    headline="Nightt!"
    return render_template("index.html", headline=headline)
