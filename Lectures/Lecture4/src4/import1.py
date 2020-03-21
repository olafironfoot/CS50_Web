import csv
import os

from flask import Flask, render_template, request
from models import *

#equating app to Flask module, giving it propreties like app.config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ("postgres://ufahdppxmwmnfk:e0c55691f4045b71ca10ca5fad61e91027d9131fb8c7904142dcb0677f2a4a2e@ec2-23-21-13-88.compute-1.amazonaws.com:5432/d2vbqq75absh07")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#ties the database with app (db is located in models.py imported in line 5)
db.init_app(app)

#these are the functions the computer runs
def main():
    #opens and reads flight.csv
    f = open("flights.csv")
    #olaf:Return a object which will iterate over lines in the given csvfile.
    reader = csv.reader(f)
    for i in reader:
        print(i)
    #olaf: using python. for every line in the object, because of the csv.reader() function, every line is now a list.
    for origin, destination, duration in reader:
        #olaf:create an object 'flight' under the class Flight and give it variables, origin, destination and duration)
        flight = Flight(origin=origin, destination=destination, duration=duration)
        #olaf:add it into the data base
        db.session.add(flight)
        #olaf:print the files added
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    #olaf:execute the above and commit
    db.session.commit()

if __name__ == "__main__":
    #olaf: this allows us to interact with our flask application on commandline
    with app.app_context():
        main()
