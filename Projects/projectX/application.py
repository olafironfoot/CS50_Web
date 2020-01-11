from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getStarted")
def getStarted():
    return render_template("getStarted.html")

@app.route("/Learners")
def Learners():
    return render_template("Learners.html")

@app.route("/LevelsOfLearning")
def LevelsOfLearning():
    return render_template("LevelsOfLearning.html")

@app.route("/hello", methods=["POST"])
def hello():

    # OrderOfLearning & Objectives are from getStarted.html form
    nameHello_py = request.form.get("OrderOfLearning")
    nameHello_py2 = request.form.get("Objectives")
    # QUETION: How does this python code know where to look to get those attributes?
    # does it know to trace back to the page before /hello, in this case the getStarted page?

    return render_template("hello.html", nameAH=nameHello_py)
