#!/usr/bin/env python3
"""
Basic Flask app with Babel integration and locale selection
"""

from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """
    Render the 3-index.html template with a welcome message
    """
    home_title = "Welcome to Holberton"
    home_header = "Hello world!"
    return render_template(
        "3-index.html", home_title=home_title, home_header=home_header
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
