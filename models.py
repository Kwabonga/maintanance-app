from . import db
from flask_login import UserMixin
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy



#database for storing the querys
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placeof= db.Column(db.String(100))
    blockof= db.Column(db.String(100))
    problem= db.Column(db.String(1000))
    date= db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='reports')


#sign up user data base
class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(100), unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    reports=db.relationship('Report')


