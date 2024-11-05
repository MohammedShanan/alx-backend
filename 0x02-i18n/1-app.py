#!/usr/bin/env python3
"""
Basic Flask app with Babel integration.
"""

from flask import Flask, render_template
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


@app.route("/")
def index() -> str:
    """
    Render the 1-index.html template with a welcome message
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
