from flask import Blueprint, render_template, flash, redirect
from flask_login import login_required, current_user
from .models import Seat
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
@login_required
def home():
    """Creates the home page of the website."""
    return render_template("home.html", user=current_user)


@views.route('/bookingsystem', methods=['GET'])
@login_required
def bookingsystem():
    """Creates the booking-system page where users can choose the flight they want to book a seat on."""
    flights = Seat.query.filter_by(seat_row='1', seat_column='A').all()
    return render_template('bookingsystem.html', user=current_user, flights=flights)


@views.route('/help', methods=['GET'])
@login_required
def help_page():
    """Creates the help page where users find information about how the booking-system works."""
    return render_template('help.html', user=current_user)


@views.route('/flight/<int:flights>', methods=['GET'])
@login_required
def flight(flights):
    """Creates the page where the seat layout of the previously chosen flight is displayed."""
    seat_to_render = Seat.query.filter_by(seat_flight=flights)
    row_number = Seat.query.filter_by(seat_flight=flights, seat_column='A').all()
    list_of_rows = []
    for i in range(len(row_number)+1):
        row = Seat.query.filter_by(seat_flight=flights, seat_row=i)
        list_of_rows.append(row)

    return render_template('seats.html', user=current_user, seat_to_render=seat_to_render, list_of_rows=list_of_rows)


@views.route('/flight/<int:flights>/booking-seat/<int:id>', methods=['GET'])
@login_required
def booking_seat(flights, id):
    """Lets user book a seat when clicking on it and confirming their choice."""
    booked_seat = Seat.query.get_or_404(id)
    booked_seat.seat_status = 'False'
    booked_seat.user_id = current_user.id
    try:
        db.session.commit()
        flash('Seat booked successfully!', category='success')
    except:
        flash('An error occurred while booking your seat', category='error')
    return redirect('/flight/'+str(flights))


@views.route('/flight/<int:flights>/cancel-seat/<int:id>', methods=['GET'])
@login_required
def cancel_seat(flights, id):
    """Lets user cancel the reservation of a seat by clicking on it and confirming the cancellation."""
    canceled_seat = Seat.query.get_or_404(id)
    canceled_seat.seat_status = 'True'
    canceled_seat.user_id = 'None'
    try:
        db.session.commit()
        flash('Seat canceled successfully!', category='success')
    except:
        flash('An error occurred while canceling your seat', category='error')
    return redirect('/flight/'+str(flights))
