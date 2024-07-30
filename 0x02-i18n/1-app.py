#!/usr/bin/env python3
"""Basic Babel setup."""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app=app)


@app.route('/')
def index():
    """The home route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
