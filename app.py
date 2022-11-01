import os

import tweepy
from flask import Flask, redirect, request

app = Flask(__name__)
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_secret)


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

    # Adding this here to test API.
    # Need to be sent to the homepage from here if verified
    user = tweepy.API(auth, wait_on_rate_limit=True)
    return user.verify_credentials().name


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
