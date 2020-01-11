from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/david")
def david():
    return "Hello, David!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return "<h1>Hello weee manhuirewh, {}!</h1>".format(name)
