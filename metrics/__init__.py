import os
import tweepy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
flask_secret = os.environ.get("FLASK_SECRET")
sql_alchemy_uri = os.environ.get("SQLALCHEMY_DATABASE_URI")

app = Flask(__name__)
app.config["SECRET_KEY"] = flask_secret
app.config["SQLALCHEMY_DATABASE_URI"] = sql_alchemy_uri
db = SQLAlchemy(app)

auth = tweepy.OAuth1UserHandler(api_key, api_secret)

from metrics import routes
