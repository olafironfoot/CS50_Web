import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#olaf: encryption using pbkdf2 and scrypt (Source: https://www.vitoshacademy.com/hashing-passwords-in-python/)
import hashlib, binascii, os


db = SQLAlchemy()

##olaf: simple authentication (source: https://gist.github.com/jslvtr/139cf76db7132b53f2b20c5b6a9fa7ad)
# class User:
#     def __init__(self, username, password):
#         self.username = userNameVariableInApplication_py
#         self.password = passwordVariableInApplication_py
#
#     def save_to_db(self):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()
#
#         try:
#             cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (self.username, self.password))
#         except:
#             cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
#             raise UserNotFoundError('The table `users` did not exist, but it was created. Run the registration again.')
#         finally:
#             connection.commit()
#             connection.close()

#olaf: encryption using pbkdf2 and scrypt (Source: https://www.vitoshacademy.com/hashing-passwords-in-python/)
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

#olaf: Usage - of encryption using pbkdf2 and scrypt (Source: https://www.vitoshacademy.com/hashing-passwords-in-python/)
# stored_password = hash_password('ThisIsAPassWord')
# print(stored_password)
#
# print(verify_password(stored_password, 'ThisIsAPassWord'))
#
# print(verify_password(stored_password, 'WrongPassword'))


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    passengers = db.relationship("Passenger", backref="flight", lazy=True)

    def add_passenger(self, name):
        p = Passenger(name=name, flight_id=self.id)
        db.session.add(p)
        db.session.commit()


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
