from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    birth_date = db.Column(db.DateTime)
    role = db.Column(db.String(10))
    seats = db.relationship('Seat')


class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seat_flight = db.Column(db.String(10))
    seat_row = db.Column(db.String(5))
    seat_column = db.Column(db.String(5))
    seat_status = db.Column(db.String(10))
    seat_type = db.Column(db.String(10))
    seat_unique = db.Column(db.String(20), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
