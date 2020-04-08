from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


tags = db.Table('tags',
                db.Column('user_id', db.Integer, db.ForeignKey('user.id'),
                          primary_key=True),
                db.Column('authentication_id', db.Integer,
                          db.ForeignKey('authentication.id'), primary_key=True)
                ,
                db.Column('authorization_id'), db.Integer,
                db.ForeignKey('authorization.id'), primary_key=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    pass_hash = db.relationship('Authentication')


class Authentication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass_hash = db.Column(db.String, nullable=False)
    # add 2fa maybe a hint? etc etc


class Authorization(db.Model):
    id = db.Column(db.Integer,)
    admin = db.Column(db.String,)
