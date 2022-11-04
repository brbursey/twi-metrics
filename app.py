import os

import tweepy
from flask import Flask, redirect, render_template, request, session
from tweepy import API

from db import Session
from metrics import DM, Metrics
from models import User

app = Flask(__name__)

api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
auth = tweepy.OAuth1UserHandler(api_key, api_secret)

conn = Session()


# @app.route("/")
# def start():
#     return render_template("login.html")


# @app.route("/login", methods=["POST"])
# def login():
#     email = request.form["email"]
#     password = request.form["password"]

#     user = conn.query(User).filter_by(email=email)

#     session["email"] = email
#     session["password"] = password

#     print(user)

#     if not user:
#         return redirect("/authorize")

#     return redirect("home/")


@app.route("/authorize")
def authorize():
    """Sends user to to authorize app page in twitter."""

    return redirect(auth.get_authorization_url(signin_with_twitter=True))


@app.route("/callback", methods=["GET", "POST"])
def callback():
    """
    Once the user clicks authorize, gets the oauth_verifier
    and authorizes the app to access their twitter
    """

    oauth_token = request.args.get("auth_token", None)
    oauth_verifier = request.args.get("oauth_verifier", None)
    access_token, access_token_secret = auth.get_access_token(oauth_verifier)
    # api = API(auth)
    # twitter_user = api.verify_credentials()

    # user = User(
    #     name=twitter_user.name,
    #     email=session["email"],
    #     twitter_id=twitter_user.id,
    #     authorized=True,
    # )
    # session["user"] = user
    # conn.add(user)

    return redirect("/home")


@app.route("/home")
def home():
    api = API(auth)
    twitter_user = api.verify_credentials()

    return f"Welcome to twitter-metrics, {twitter_user.name}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
