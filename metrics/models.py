from flask import Flask
from metrics import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    twitter_id = db.Column(db.Integer, unique=True, nullable=False)
    authorized = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.twitter_id}', '{self.authorized}')"



class DM(Base):
    __tablename__ = "dms"

    id = Column(Integer, primary_key=True)
    

class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True)

