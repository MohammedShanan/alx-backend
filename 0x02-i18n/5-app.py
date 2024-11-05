#!/usr/bin/env python3
"""
Basic Flask app with Babel integration and locale selection
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Config class for Flask app
    Defines available languages and default locale and timezone
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


@app.context_processor
def inject_translator():
    return {"_": _}


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed"""
    try:
        u_id = request.args.get("login_as")
        return users.get(int(u_id))
    except Exception:
        return


@app.before_request
def before_request():
    """use get_user to find a user if any, and set it as a global on
    flask.g.user"""
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """
    Render the 5-index.html template with a welcome message
    """
    home_title = "Welcome to Holberton"
    home_header = "Hello world!"
    return render_template(
        "5-index.html", home_title=home_title, home_header=home_header
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
