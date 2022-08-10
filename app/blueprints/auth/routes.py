from app import db
from app.blueprints.auth.forms import LoginForm, RegistrationForm
from app.blueprints.main.models import User
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from . import bp as app


@app.route('/login', methods=['get', 'post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    print(form.password.data)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('No user with that username.')
            return redirect(url_for('auth.login'))
        elif not user.check_password(form.password.data):
            flash('Invalid password.')
            return redirect(url_for('auth.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.home')
        return redirect(url_for('main.home'))
    return render_template('auth/login.html', form=form)


@app.route('/register', methods=['get', 'post'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
