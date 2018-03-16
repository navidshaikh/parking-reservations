from flask import request, jsonify
from app import app, db, ma
from models import User, Slot, Reservation


@app.route("/")
@app.route("/index")
def index():
    return "Hello from Parking Reservations Flask App!"


@app.route("/user", methods=["POST"])
def add_user():

    json_data = request.get_json()
    print "Received JSON via /user POST"
    print json_data
    username = json_data["username"]
    email = json_data["email"]

    new_user = User(username, email)
    db.session.add(new_user)
    db.session.commit()

    return "Added!"


@app.route("/slot", methods=["POST"])
def add_parking_slot():

    json_data = request.get_json()
    print "Received JSON via /slot POST"
    print json_data

    lat = json_data["lat"]
    lng = json_data["lng"]
    available = json_data.get("available", True)

    new_slot = Slot(lat, lng, available)
    db.session.add(new_slot)
    db.session.commit()

    return "Added slot."


@app.route("/make_reservation", methods=["POST"])
def make_reservation():
    pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9090)
