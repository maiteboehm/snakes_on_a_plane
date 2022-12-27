from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db

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

@admins.route('/user/update-user/<int:id>', methods=['GET','POST'])
@login_required
def update_user(id):
    user_to_update = User.query.get_or_404(id)
    if request.method == 'POST':
        user_to_update.email = request.form['email']
        user_to_update.first_name = request.form['first_name']
        user_to_update.last_name = request.form.get['last_name']
        user_to_update.role = request.form.get['role']
        try:
            db.session.commit()
            flash('Account updated!', category='success')
            return redirect(url_for('admins.admin_user'))
        except:
            flash('Account not updated!', category='error')
            return render_template('update_user.html', user= current_user, user_to_update=user_to_update)

    return render_template('update_user.html', user= current_user, user_to_update=user_to_update)

