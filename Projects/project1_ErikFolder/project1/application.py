import os

from flask import Flask, session, render_template, jsonify, request, url_for, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

from markupsafe import escape


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

#olaf: create a login page that has a form, containing "login" & "register" button
@app.route("/")
def index():
    """Provide fields for login"""
    if request.method=="POST":
        return render_template("success.html", message="logged in from index to success page")

    if 'username' in session:
        return render_template("searchForm.html")

        # return 'Logged in as %s' % escape(session['username'])
    return render_template("index.html", message="not logged in")


@app.route("/searchForm", methods=["POST"])
def searchForm():
    """provide form to recieve user input"""
#olaf: need a form or HTML that allows people to fill in what they are searching for
    return render_template("searchForm.html")





@app.route("/search", methods=["POST"])
def search():
    """Search for books"""

    #olaf: pass the search field as a SQL command into database and return the result
        #olaf: display the result back into the HTML by using a list and loop
    if request.method == "POST":
        if request.form['submit_button'] == "search":
            searchBookVariableOnApplication_py=request.form['searchBook']

            if searchBookVariableOnApplication_py == "":
                return render_template("error.html", message="no search fields provided")

            # found = db.execute("SELECT * FROM books_table WHERE isbn OR title OR author OR year LIKE '%lookingFor= :lookingFor%' ", {"lookingFor": searchBookVariableOnApplication_py}).fetchall()

            # best example, but no data passed:
            found = db.execute("SELECT * FROM books_table WHERE (isbn ILIKE :lookingFor) OR (title ILIKE :lookingFor) OR (author ILIKE :lookingFor) OR (year::text ILIKE :lookingFor)",
            {"lookingFor": f"%{searchBookVariableOnApplication_py}%"}).fetchall();

             #working code:
             # found = db.execute("SELECT * FROM books_table WHERE isbn LIKE '%' || :lookingFor || '%'", {"lookingFor": f"{searchBookVariableOnApplication_py}"}).fetchall();


            # olaf:tried striping and doing literal ||, did not work, same issue:
            #found = db.execute("SELECT * FROM books_table WHERE (isbn LIKE '%'||:lookingFor||'%') OR (title LIKE '%||:lookingFor||%') OR (title LIKE '%||:lookingFor||%') OR (year::text LIKE '%||:lookingFor||%')", {'lookingFor': searchBookVariableOnApplication_py.strip("\'")}).fetchall();


            #olaf: working code without variables
            #found = db.execute("SELECT * FROM books_table WHERE (isbn LIKE '%123%') OR (title LIKE '%123%') OR (title LIKE '%123%') OR (year::text LIKE '%2012%')");
            return render_template("search.html", found=found)


        elif request.form['submit_button'] == 'logout':
            return redirect(url_for('logout'))






@app.route("/search/<int:book_id>")
def book(book_id):
    """List details about a single book."""

    # Make sure book exists.
    book = db.execute("SELECT * FROM books_table WHERE id = :id", {"id": book_id}).fetchone()
    if book is None:
        return render_template("error.html", message="No such book.")

    # Get review infomation on book
    # review_table = db.execute("SELECT isbn, title, author, year FROM books_table WHERE book_id = :book_id",
    #                         {"book_id": book_id}).fetchall()
    return render_template("book.html", book=book)
    #olaf: to be implemented when review table is ready: return render_template("book.html", book=book, passengers=passengers)





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
    session['username'] = request.form['userNameFromHTML']

    return render_template("success.html", message="logged in from sign in, session assigned!")



@app.route("/logout", methods=["POST", "GET"])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    # return redirect(url_for('success.html'))
    return render_template("logout.html", message="logged out!")

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
    if request.form['userNameFromHTML'] == "":
        return render_template("error.html", message="username cannot be blank")
    if request.form['passwordFromHTML'] != request.form['passwordConfirmationFromHTML']:
        return render_template("error.html", message="password does not match")
    if request.form['passwordFromHTML'] == None:
        return render_template("error.html", message="password cannot be blank")
    if request.form['passwordConfirmationFromHTML'] == None:
        return render_template("error.html", message="password confirmation cannot be blank")


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
