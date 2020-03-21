import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    #olaf: This is a function now under the class, Flight
    def add_passenger(self, name):
        #olaf: This is a function that allows user to add Passenger(along with name & behind the scenes flight_id under .id attribute) and equate it to the variable "p"
            #olaf: flight_id is the id of whatever the flight is, tagged to the passenger defined by name(E.g. f1.add_passenger(John) will give the f1's flight id as an attribute stored under John.id)
        p = Passenger(name=name, flight_id=self.id)
        #olaf: adds the passenger to and commmit them to the database.
        db.session.add(p)
        db.session.commit()


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
