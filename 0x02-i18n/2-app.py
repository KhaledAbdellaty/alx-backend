#!/usr/bin/env python3
"""Basic Babel setup."""
from flask_babel import Babel
from flask import Flask, request


class Config:
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app=app)


@babel.localeselector
def get_locale():
    """A function that determine the best
    match with our supported languages."""
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run()
