from datetime import date
from flask import flash, redirect, url_for

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
def admin_user_check(current_user):
    if current_user.role == 'admin':
        return True
    else:
        flash('You need do be an Admin to access!!', category='error')
        return redirect(url_for('views.home'))
