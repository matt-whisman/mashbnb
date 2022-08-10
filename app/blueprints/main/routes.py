import requests
from app import db
from app.blueprints.main.forms import SearchForm
from app.blueprints.main.models import User
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from . import bp as app


@app.route('/')
def home():
    return render_template('index.html')


