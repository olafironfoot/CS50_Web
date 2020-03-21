import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ufahdppxmwmnfk:e0c55691f4045b71ca10ca5fad61e91027d9131fb8c7904142dcb0677f2a4a2e@ec2-23-21-13-88.compute-1.amazonaws.com:5432/d2vbqq75absh07"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    #insert (multiple lists?) into the variable flights
    flights = Flight.query.all()
    print(flights)
    print(f"printing the object(flights for instance) we need to make sure it is a python type(int, list, string ect.) -> {Flight.query.all()}. If we want We need to loop through the object if we want human readable values")
    #loop across each item within the variable and print it
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    for i in flights:
        print(f"Looping through without dot operator only gives flight ID: {i}") #without the.operators it only prints out the primary key "flight1"

if __name__ == "__main__":
    with app.app_context():
        main()
