from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ufahdppxmwmnfk:e0c55691f4045b71ca10ca5fad61e91027d9131fb8c7904142dcb0677f2a4a2e@ec2-23-21-13-88.compute-1.amazonaws.com:5432/d2vbqq75absh07"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#olaf:"relates app(along with all it's attributes like app.config) to db.init_app"
db.init_app(app)

#olaf: go to the home/root page
@app.route("/")
def index():
    #equate all of flight table to the variable flights
    flights = Flight.query.all()
    #render index page and passing in the variable flights
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information.
    #olaf: pass the infomation into the variable name what end user fills in. (to call it later when adding passenger)
    name = request.form.get("name")
    #olaf: make sure the flight id exists within the drop down they pick
    try:
        #olaf: pass the infomation into the variable name what end user picks. (to call it later when adding passenger)
        flight_id = int(request.form.get("flight_id"))
    #olaf: otherwise, render error page
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists. #olaf: by asking the database if the flight exsist
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight with that id.")

    # Add passenger.
    passenger = Passenger(name=name, flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    return render_template("success.html")

#see all flights
@app.route("/flights")
def flights():
    """List all flights."""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

#olaf: open a site with a variable URl
@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a single flight."""

    # Make sure flight exists.
    #olaf: pass in flight_id data from Database to the variable flight
    flight = Flight.query.get(flight_id)
    if flight is None:
        #olaf: if none, show error site
        return render_template("error.html", message="No such flight.")

    # Get all passengers. #olaf: filter and past through all passengers under that flight_id. pass data to HTML page during render.
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template("flight.html", flight=flight, passengers=passengers)
