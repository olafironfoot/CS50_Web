from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   #Olaf:"creates a database"

class Flight(db.Model): #Olaf:"defines a class, but QN: what does db.Model do - suspect it adds more propreties to our flight class, like "Flight.query.all()"(see 37:33 of youtube lecture)"
    __tablename__ = "flights"   #Olaf:"names the table"
    id = db.Column(db.Integer, primary_key=True)    #Olaf:"creates an object under the class Flight which requires arguments from "db.Model"(probably a variable in SQL Alchemy that contants argument names). And by using SQLAlchemy package, give it attributes, db.Integer, and primary_key, then linking it to the python variable `id` "
    origin = db.Column(db.String, nullable=False)   #Olaf:"creates an object(under class Flight), setting db.Column's variables before passing it into `Origin` "
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)  #Olaf:"creates an object with similar attributes passed in except for an addition attribute/proprety db.ForeignKey("flight.id")"
