import os
#olaf: from flask documentation, added "redirect, url_for" https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
from flask import Flask, session, render_template, jsonify, request, redirect, url_for
from flask_session import Session

#olaf: from flask documentation https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
from markupsafe import escape

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *


app = Flask(__name__)

app.secret_key =

#from the internet...# app.config['DATABASE_URL'] = "path_to_db"


# Check for environment variable
if not "postgres://ufahdppxmwmnfk:e0c55691f4045b71ca10ca5fad61e91027d9131fb8c7904142dcb0677f2a4a2e@ec2-23-21-13-88.compute-1.amazonaws.com:5432/d2vbqq75absh07":
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://ufahdppxmwmnfk:e0c55691f4045b71ca10ca5fad61e91027d9131fb8c7904142dcb0677f2a4a2e@ec2-23-21-13-88.compute-1.amazonaws.com:5432/d2vbqq75absh07")
db = scoped_session(sessionmaker(bind=engine))

#olaf: create a login page that has a form, containing "login" & "register" button
@app.route("/")
def index():
#olaf: from flask documentation https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


    #olaf: check login user name and password against database
        #olaf: if username & password is true, bring them to success page/home page
            #if not, return error message

    return render_template("index.html")

#olaf: Login button
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route("/register", methods=["POST"])
def register():
    """Register for the site"""

    return render_template("auth/registerHere.html")

@app.route("/registered", methods=["POST"])
def registered():
    """User clicked register and now has to check if:
    - password matches
    - Username duplicates
    else:
        register them into the database and hash the password"""

    userNameVariableInApplication_py = request.form['userNameFromHTML']
    passwordVariableInApplication_py = hash_password(request.form['passwordFromHTML'])
    passwordConfirmationVariableInApplication_py = hash_password(request.form['passwordConfirmationFromHTML'])

#olaf: Usage - of encryption using pbkdf2 and scrypt (Source: https://www.vitoshacademy.com/hashing-passwords-in-python/)
# stored_password = hash_password('ThisIsAPassWord')
# print(stored_password)
#
# print(verify_password(stored_password, 'ThisIsAPassWord'))
#
# print(verify_password(stored_password, 'WrongPassword'))
    #olaf: encrypted way of checking password match
    if request.form['passwordFromHTML'] != request.form['passwordConfirmationFromHTML']:
        return render_template("error.html", message="password does not match")

    # #olaf: non-encrypt way of check that passwords matches
    # if passwordVariableInApplication_py != passwordConfirmationVariableInApplication_py:
    #     return render_template("error.html", message="password does not match")

# olaf: from airline1/application.py
    #olaf: if rowcount > 0 (user already exist), give error message
    if db.execute("SELECT * FROM usersAndPasswords_table WHERE userName = :userName", {"userName": userNameVariableInApplication_py}).rowcount > 0:
        return render_template("error.html", message="Username already exisit, pick another username")


#olaf: insert name and password into the usersAndPasswords_table
    db.execute("INSERT INTO usersAndPasswords_table (username, password) VALUES (:username, :password)",
            {"username": userNameVariableInApplication_py, "password": passwordVariableInApplication_py})
    db.commit()
    return render_template("success.html", message="You're registered! Click on the button below go back and sign in.")
# olaf: End of from airline1/application.py




##olaf: Login button
# @app.route("/login", methods=["POST"])
# def login():
#     """Register for the site"""
#
#     # Get form information.
#     name = request.form.get("name")
#     try:
#         flight_id = int(request.form.get("flight_id"))
#     except ValueError:
#         return render_template("error.html", message="Invalid flight number.")
#
#     # Make sure the flight exists.
#     flight = Flight.query.get(flight_id)
#     if not flight:
#         return render_template("error.html", message="No such flight with that id.")
#
#     # Add passenger.
#     flight.add_passenger(name)
#     return render_template("success.html")
