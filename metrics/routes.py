import tweepy
from flask import Flask, flash, redirect, render_template, request, session, url_for
from metrics import app, auth
from metrics.forms import LoginForm, RegistrationForm


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    If the user is new, lets the user sign up for an account. 
    Redirects to auth afterwards.
    """

    form = RegistrationForm()
    if form.validate_on_submit():
        # TODO: Store info in db
        return redirect(url_for("authorize"))

    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    """Login page for users"""
    
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))

    return render_template("login.html", title="Register", form=form)


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

    return redirect("/home")


@app.route("/home")
def home():
    api = tweepy.API(auth)
    twitter_user = api.verify_credentials()

    return "Welcome to twitter-metrics!"
