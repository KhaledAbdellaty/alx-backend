#!/usr/bin/env python3
"""Basic Babel setup."""
from flask_babel import Babel
from flask import Flask, request, render_template


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app=app)


@babel.localeselector
def get_locale():
    """A function that determine the best
    match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
