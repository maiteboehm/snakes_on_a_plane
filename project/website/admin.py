from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Seat
from .python_scripts import admin_user_checker
from . import db
from .CharReader import Dictionary_Creater
from .CharReader import model_seat_filler
import os


admins = Blueprint('admins', __name__)

@admins.route('/', methods=['GET','POST'])
@login_required
def admin_home():
    admin = admin_user_checker(current_user)
    if admin:
        return render_template('admin_home.html', user= current_user)


@admins.route('/user', methods=['GET', 'POST'])
@login_required
def admin_user():
    admin = admin_user_checker(current_user)
    if admin:
        users = User.query.all()
        return render_template('admin_user.html', user=current_user, users=users)

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
    admin = admin_user_checker(current_user)
    if admin:
        user_to_delete = User.query.get_or_404(id)
        seat_to_change = Seat.query.filter_by(user_id = id).all()
        for change in seat_to_change:
            change.seat_status = 'True'
        try:
            db.session.delete(user_to_delete)
            db.session.commit()
            flash('Account deleted!', category='success')
            return redirect('/admin-area/user')
        except:
            flash('Account NOT deleted!', category='error')
            return redirect('/admin-area/user')

@admins.route('/update-flights', methods=['GET','POST'])
@login_required
def admin_flights():
    admin = admin_user_checker(current_user)
    if admin:
        Path = os.path.abspath(os.curdir)
        ChartIn_Path = Path +'\Input_Data\\'
        Flight_Dictionary = Dictionary_Creater(ChartIn_Path)
        model_seat_filler(Flight_Dictionary)
        return redirect('/admin-area/seats')

@admins.route('/seats', methods=['GET', 'POST'])
@login_required
def admin_seats():
    admin = admin_user_checker(current_user)
    if admin:
        seats = Seat.query.all()
        return render_template('admin_seats.html', user=current_user, seats=seats)

@admins.route('/seats/update-seats/<int:id>', methods=['GET','POST'])
@login_required
def update_seat(id):
    admin = admin_user_checker(current_user)
    if admin:
        seat_to_update = Seat.query.get_or_404(id)
        if request.method == 'POST':
            seat_to_update.user_id = request.form['user_id']
            if seat_to_update.user_id == '' or seat_to_update.user_id =='None':
                seat_to_update.seat_status = 'True'
            else:
                seat_to_update.seat_status = 'False'
            try:
                db.session.commit()
                flash('Account updated!', category='success')
                return redirect('/admin-area/seats')
            except:
                flash('Account NOT updated!', category='error')
                return redirect('/admin-area/seats')
        else:
            return render_template('admin_update_seat.html', user= current_user, seat_to_update=seat_to_update)

@admins.route('/statistics', methods=['GET','POST'])
@login_required
def admin_statistics():
    admin = admin_user_checker(current_user)
    if admin:
        return render_template('admin_statistics.html', user = current_user)

