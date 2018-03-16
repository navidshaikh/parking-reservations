from flask import request, jsonify
from app import app, db
from models import User, Slot, Reservation
from models import UserSchema, SlotSchema, ReservationSchema


user_schema = UserSchema(many=True)
slot_schema = SlotSchema(many=True)
res_schema = ReservationSchema(many=True)


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


@app.route("/get_slot", methods=["GET"])
def get_available_slots():
    available_slots = Slot.query.filter_by(available=True).all()
    result = slot_schema.dump(available_slots)
    print "Available slots.."
    print result.data
    return jsonify(result.data)


@app.route("/users", methods=["GET"])
def get_all_users():
    all_users = User.query.all()
    result = user_schema.dump(all_users)
    print "Available all users.."
    print result.data
    return jsonify(result.data)


@app.route("/make_reservation", methods=["POST"])
def make_reservation():
    return "To be implemented"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9090)
