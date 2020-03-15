from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   #Olaf:"creates a database"

class Flight(db.Model): #Olaf:"defines a class, but QN: what does db.Model do"
    __tablename__ = "flights"   #Olaf:"names the table"
    id = db.Column(db.Integer, primary_key=True)    #Olaf:"creates an object using the SQLAlchemy class/package and giving it attributes, db.Integer, and setting primary_key as True, then linking it to the python variable id"
    origin = db.Column(db.String, nullable=False)   #Olaf:""
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
