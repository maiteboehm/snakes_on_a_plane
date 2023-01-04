from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from .models import User
from .Statistics import database_reader
from . import db

from .python_scripts import new_user_checker

auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """Creates the sign-up pages on which new users can log in."""
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        birth_date = request.form.get('birth_date')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        role = 'user'
        user_to_check = new_user_checker(email, first_name, last_name, birth_date, password1, password2)

        # if the user check is passed a new user will be added to the user-database and logged in.
        if user_to_check:
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
            new_user = User(email=email, first_name=first_name, last_name=last_name, birth_date=birth_date,
                            password=generate_password_hash(password1, method='sha256'), role=role)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

            flash('Account created!', category='success')

            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Creates the login page on which the users where the user can log in."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    """Logs the user out and ends the session.After logging out the user will redirected to the login page."""
    logout_user()
    database_reader(Seat)
    flash('Logged out successfully! Thank you for traveling with Snakes on a Plane!!', category='success')
    return redirect(url_for('auth.login'))
