Parking reservation REST API
===========================


```
export FLASK_APP=parking_reservations.py
flask db init
flask db migrate
flask db upgrade
flask run
```


Load data in database
=====================
```
In [2]: from app.models import User, Slot, Reservation

In [3]: u = User(username="navid", email="m1@mail.com")

In [4]: from app import db

In [5]: db.session.add(u)

In [6]: db.session.commit()

In [7]: print User.query.all()
[<User navid >]

In [9]: s = Slot(lat="11.12345",lng="12.12345",available=True)

In [10]: db.session.add(s)

In [11]: db.session.commit()

In [12]: print Slot.query.all()
[<Slot 1>]

```
