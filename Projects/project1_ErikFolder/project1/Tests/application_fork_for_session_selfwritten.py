import os

from flask import Flask, session, render_template, jsonify, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *


app = Flask(__name__)

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
session={"default_user_id":0,  "loggedIn_user_id":0}

@app.route("/login", methods=["POST"])
def login():
    """Login to site"""

    userNameVariableInApplication_py = request.form['userNameFromHTML']
    # passwordVariableInApplication_py = request.form['passwordFromHTML']

    #olaf: Mistake and lesson, used fetchall which returned an object within a list. fetchone returns the object so we can use the attribute, ie. password attribute. documentation here https://docs.sqlalchemy.org/en/13/core/connections.html#sqlalchemy.engine.RowProxy
    row = db.execute("SELECT * FROM usersAndPasswords_table WHERE username = :username", {"username": userNameVariableInApplication_py}).fetchone()

    #olaf: check login user name and password against database
    if row is None or row.id<1 or not (verify_password(row.password, request.form['passwordFromHTML'])):
        return render_template("error.html", message="invalid login details")
        #olaf: if username & password is true, log them into a session and bring them to success page/home page
            #if not, return error message
    session["loggedIn_user_id"] = row.id

    return render_template("success.html", messawge="logged in from sign in, session assigned!")


#olaf: create a login page that has a form, containing "login" & "register" button
@app.route("/")
def index():
    #olaf: check if it is the same user
    if session['default_user_id'] == 0 :
        return render_template("index.html", message="not logged in")
    if session["loggedIn_user_id"] == row.id :
        return render_template("success.html", message = "logged in from exisiting session")

@app.route('/logout')
def logout():
    session.pop("user_id", None)
    return redirect(url_for('index'))

#olaf: Login button
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
