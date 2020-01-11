import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year_py = now.month == 1 and now.day == 1

    names_py = ["Alice", "Bob", "Charlie", "David"]

    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("index.html", new_yearVarFromPython=new_year_py, textVarDefinedInPythonToHTML="Name", listVarLinkedFromPythonToHTML=names_py, notes=notes)


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
