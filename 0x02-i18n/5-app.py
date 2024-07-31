#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel
"""Mock logging in"""

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app=app)


def get_user():
    """A function that returns a user dictionary or None """
    if request.args.get('login_as'):
        id = int(request.args.get('login_as'))
        if id in users:
            return users[id]
    return None


@app.before_request
def before_request():
    """Finds user and sets as global on flask.g.user"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """A function that determine the best
    match with our supported languages."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """The home/index page.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
