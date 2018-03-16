import os
basedir = os.path.abspath(os.path.dirname(__file__))

db_filename = "park.sqlite"

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
            basedir, db_filename)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

