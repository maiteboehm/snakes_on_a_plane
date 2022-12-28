from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Seat
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

@admins.route('/user', methods=['GET', 'POST'])
@login_required
def admin_user():
    if current_user.role == 'admin':
        users = User.query.all()
        return render_template('admin_user.html', user=current_user, users=users)
    else:
        flash('You need do be an Admin to access!!', category='error')
        return redirect(url_for('views.home'))

@admins.route('/user/update-user/<int:id>', methods=['GET', 'POST'])
@login_required
def update_user(id):
    user_to_update = User.query.get_or_404(id)
    if request.method == 'POST':
        user_to_update.email = request.form['email']
        user_to_update.first_name = request.form['first_name']
        user_to_update.last_name = request.form['last_name']
        user_to_update.role = request.form['role']
        try:
            db.session.commit()
            flash('Account updated!', category='success')
            return redirect('/admin-area/user')
        except:
            flash('Account NOT updated!', category='error')
            return redirect('/admin-area/user')
    else:
        return render_template('admin_update_user.html', user= current_user, user_to_update=user_to_update)

@admins.route('user/delete-user/<int:id>',methods=['POST', 'GET'])
@login_required
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash('Account deleted!', category='success')
        return redirect('/admin-area/user')
    except:
        flash('Account NOT deleted!', category='error')
        return redirect('/admin-area/user')
@admins.route('/seats', methods=['GET', 'POST'])
@login_required
def admin_seats():
    if current_user.role == 'admin':
        seats = Seat.query.all()
        return render_template('admin_seats.html', user=current_user, seats=seats)
    else:
        flash('You need do be an Admin to access!!', category='error')
        return redirect(url_for('views.home'))


