from flask import Flask, Blueprint, render_template, request
from flask_login import login_required, current_user
from .python_scripts import write_seats_html
from .models import Seat

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/bookingsystem', methods=['GET','POST'])
@login_required
def bookingsystem():
    Flights = Seat.query.filter_by(seat_row='1', seat_column='A').all()
    return render_template('bookingsystem.html', user=current_user, flights= Flights)

@views.route('/help', methods=['GET','POST'])
@login_required
def help():
    return render_template('help.html', user=current_user)


@views.route('/flight/<int:flights>', methods=['GET','POST'])
def flight(flights):
   flight_to_render = Seat.query.filter_by(flight = flights)
   return render_template('seats.html', user = current_user, flight_to_render= flight_to_render)

@views.route('/seats', methods=['GET', 'POST'])
@login_required
def seats():
    if request.method == 'GET':
        with open(r'Input_Data/chartIn2.txt', 'r') as f:
            seat_list = []
            seat_list_new = []
            for line in f:
                data = line.split('\t')
                seat_list.append(data)
                for row in seat_list:
                    row_new = []
                    for seat in row:
                        seat_new = seat.strip()
                        row_new.append(seat_new)
                seat_list_new.append(row_new)
        write_seats_html(seat_list_new, 'website/templates')

    return render_template("seats.html", user=current_user)



