from datetime import datetime

from app import db
from app import ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(40), unique=True)
    reservations = db.relationship("Reservation", backref="user", lazy="dynamic")

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
         return "<User {} >".format(self.username)



class UserSchema(ma.Schema):
    class Meta:
        fields = ("username", "email")


class Slot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    available = db.Column(db.Boolean, default=False)
    reservations = db.relationship("Reservation", backref="slot", lazy=True)

    def __init__(self, lat, lng, available=True):
        self.lat = lat
        self.lng = lng
        self.available = available


class SlotSchema(ma.Schema):
    class Meta:
        fields = ("lat", "lng", "available")


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(20))
    active = db.Column(db.Boolean, default=False)
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(db.DateTime, default=datetime.now)
    cost = db.Column(db.Float, nullable=True)
    slot_id = db.Column(db.Integer, db.ForeignKey("slot.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self):
        pass


class ReservationSchema(ma.Schema):
    class Meta:
        fields = (
                "state",
                "active",
                "start_time",
                "end_time",
                "cost",
                "slot_id",
                "user_id")
