from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required, current_user
from .models import User, Seat
from .python_scripts import admin_user_checker
from . import db
from .CharReader import dictionary_creater, model_seat_filler
from .Statistics import database_reader
import os


admins = Blueprint('admins', __name__)


@admins.route('/user', methods=['GET', 'POST'])
@login_required
def admin_user():
    """Creates the admin-user page on which the admin can see all user in the database."""
    admin = admin_user_checker(current_user)
    if admin:
        users = User.query.all()
        return render_template('admin_user.html', user=current_user, users=users)


@admins.route('/user/update-user/<int:id>', methods=['GET', 'POST'])
@login_required
def update_user(id):
    """Creates the update-user page on which the admin can update the email the name and the role"""
    admin = admin_user_checker(current_user)
    if admin:
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
            return render_template('admin_update_user.html', user=current_user, user_to_update=user_to_update)
    else:
        return redirect('/')


@admins.route('user/delete-user/<int:id>', methods=['POST', 'GET'])
@login_required
def delete_user(id):
    """Deletes the user with a given user id and changes all seats belonging to this user to free seats."""
    admin = admin_user_checker(current_user)
    if admin:
        user_to_delete = User.query.get_or_404(id)
        seat_to_change = Seat.query.filter_by(user_id=id).all()
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
    else:
        return redirect('/')

@admins.route('/update-flights', methods=['GET', 'POST'])
@login_required
def admin_flights():
    """Updates the seat database so that new input files in the folder 'Input_Data' are included."""
    admin = admin_user_checker(current_user)
    if admin:
        path = os.path.abspath(os.curdir)
        chart_in_path = path + r'\Input_Data\\'
        flight_dictionary = dictionary_creater(chart_in_path)
        model_seat_filler(flight_dictionary)
        return redirect('/admin-area/seats')
    else:
        return redirect('/')

@admins.route('/seats', methods=['GET', 'POST'])
@login_required
def admin_seats():
    """Creates an admin-seats page on which the admin can see all seats in the database."""
    admin = admin_user_checker(current_user)
    if admin:
        seats = Seat.query.all()
        return render_template('admin_seats.html', user=current_user, seats=seats)
    else:
        return redirect('/')

@admins.route('/seats/update-seats/<int:id>', methods=['GET', 'POST'])
@login_required
def update_seat(id):
    """Creates a seat update page where the administrator can change which user the seat belongs to."""
    admin = admin_user_checker(current_user)
    if admin:
        seat_to_update = Seat.query.get_or_404(id)
        if request.method == 'POST':
            seat_to_update.user_id = request.form['user_id']
            if seat_to_update.user_id == '' or seat_to_update.user_id == 'None':
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
            return render_template('admin_update_seat.html', user=current_user, seat_to_update=seat_to_update)
    else:
        return redirect('/')

@admins.route('/statistics', methods=['GET', 'POST'])
@login_required
def admin_statistics():
    """Creates a statistic page for the admin."""
    admin = admin_user_checker(current_user)
    if admin:
        flights = Seat.query.filter_by(seat_row='1', seat_column='A').all()
        free_seat_in_flight = len(Seat.query.filter_by(seat_status='True').all())
        occupied_seat_in_flight = len(Seat.query.filter_by(seat_status='False').all())
        values = [free_seat_in_flight,occupied_seat_in_flight]
        labels = ['Free seats','Occupied seats']
        colors = ["#0000FF", "#FF0000"]
        return render_template('admin_statistics.html', user=current_user, flights=flights, set=zip(values, labels, colors))
    else:
        return redirect('/')
@admins.route('/statistic/<int:flight>', methods=['GET', 'POST'])
@login_required
def admin_flight_statistic(flight):
    """Creates a statistic page for the admin."""
    admin = admin_user_checker(current_user)
    if admin:
        flights = Seat.query.filter_by(seat_row='1', seat_column='A').all()
        free_seat_in_flight = len(Seat.query.filter_by(seat_flight=flight, seat_status='True').all())
        occupied_seat_in_flight = len(Seat.query.filter_by(seat_flight=flight, seat_status='False').all())
        values = [free_seat_in_flight,occupied_seat_in_flight]
        labels = ['Free seats','Occupied seats']
        colors = ["#0000FF", "#FF0000"]
        return render_template('admin_statistic.html', user=current_user, flights=flights, flight=flight, set=zip(values, labels, colors))
    else:
        return redirect('/')

@admins.route('/refresh-statistics', methods=['Get'])
@login_required
def refresh_statistics():
    admin = admin_user_checker(current_user)
    if admin:
        database_reader(Seat)
        return redirect('/admin-area/statistics')
    else:
        return redirect('/')
