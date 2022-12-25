from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User

admins = Blueprint('admins', __name__)

@admins.route('/', methods=['GET','POST'])
@login_required
def admin_home():
    if current_user.role == 'admin':
        return render_template('admin_home.html', user= current_user)
    else:
        flash('You need do be an Admin to access!!', category='error')
        return redirect(url_for('views.home'))

@admins.route('/user', methods=['GET','POST'])
@login_required
def admin_user():
    if current_user.role == 'admin':
        users = User.query.all()
        return render_template('admin_user.html', user=current_user, users=users)
    else:
        flash('You need do be an Admin to access!!', category='error')
        return redirect(url_for('views.home'))

