import os

from flask import Flask, render_template, request
from models import *    #import stars just means to import everything, all the classes, everything.

app = Flask(__name__)       #turning app into the object, which we can exploit Flask dot operators and functions within it's documentation
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ufahdppxmwmnfk:e0c55691f4045b71ca10ca5fad61e91027d9131fb8c7904142dcb0677f2a4a2e@ec2-23-21-13-88.compute-1.amazonaws.com:5432/d2vbqq75absh07"       #one of which is config["..."] // which sets the default database URL of the object, app.config
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    #sets modification value to False
db.init_app(app)    #ties this database with app.

def main():
    db.create_all()    #creates all within file titled "models.py"

if __name__ == "__main__":
    with app.app_context(): #this allows us to interact with our flask application on commandline
        main()  #if the above fufils with the app.app_context, execute main "db.create_all()"
