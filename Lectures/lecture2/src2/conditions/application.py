import datetime
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# notesListPy = []

@app.route("/", methods=["GET", "POST"])
def index():
    now = datetime.datetime.now()
    new_year_py = now.month == 1 and now.day == 1

    names_py = ["Alice", "Bob", "Charlie", "David"]

    if session.get("notesListPy") is None:
        session["notesListPy"] = []

    if request.method == "POST":
        noteFromHtmlStoredInPyVar = request.form.get("userInput")
        session["notesListPy"].append(noteFromHtmlStoredInPyVar)

    # return render_template("index.html", notes=notes)
    return render_template("index.html", new_yearVarFromPython=new_year_py, textVarDefinedInPythonToHTML="Name", listVarLinkedFromPythonToHTML=names_py, notesForHtmlFromPy=session["notesListPy"])

@app.route("/more")
def more():
    return render_template("more.html")


@app.route("/hello", methods=["POST"])
def hello():

    # creating a python variable, nameHello_py, passing form info to that variable
    nameHello_py = request.form.get("nameFromForm")

    # line below passes the variable nameHello_py to the "nameAH" which will be reference in our hello.html file
    return render_template("hello.html", nameAH=nameHello_py)

# @app.route("/alt")
# def alt():
#     now = datetime.datetime.now()
#     new_year_py = now.month == 1 and now.day == 1
#     if new_year_py
#         text_py = yes
#     else
#         text_py = no:
#
#     return render_template("index.html", HTML_Text=text)
