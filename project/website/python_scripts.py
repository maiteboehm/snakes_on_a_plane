from datetime import date
from flask import flash, redirect, url_for
from datetime import datetime

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
def admin_user_checker(current_user):
    if current_user.role == 'admin':
        return True
    else:
        flash('You need do be an Admin to access!!', category='error')
        return redirect(url_for('views.home'))

def new_user_checker(user, email, first_name, last_name, birth_date, password1, password2):
    if birth_date == '':
        flash('Please insert your date of birth', category='error')
        age = 0
    else:
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        age = calculate_age(birth_date)
    if user:
        flash('Email already exists.', category='error')
    elif len(email) < 4:
        flash('Email must be greater than 3 characters.', category='error')
    elif len(first_name) < 2:
        flash('First name must be greater than 1 character.', category='error')
    elif len(last_name) < 2:
        flash('Last Name must be longer than one charcater', category='error')
    elif age < 18:
        flash('You must be older than 18 to create an account', category='error')
    elif password1 != password2:
        flash('Passwords don\'t match.', category='error')
    elif len(password1) < 7:
        flash('Password must be at least 7 characters.', category='error')
    else:
        return True