from flask import Flask, Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user
#from .python_scripts import write_seats_html
from .models import User, Seat
from . import db

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
@login_required
def flight(flights):
   seat_to_render = Seat.query.filter_by(flight = flights)
   row_number = Seat.query.filter_by(flight = flights, seat_column='A').all()
   list_of_rows = []
   for i in range(len(row_number)):
       row = Seat.query.filter_by(flight = flights, seat_row = i)
       list_of_rows.append(row)

   return render_template('seats.html', user = current_user, seat_to_render = seat_to_render, list_of_rows = list_of_rows)

@views.route('/flight/<int:flights>/booking-seat/<int:id>', methods=['GET', 'POST'])
@login_required
def booking_seat(flights, id):
    booked_seat = Seat.query.get_or_404(id)
    booked_seat.seat_status = 'False'
    booked_seat.user_id = current_user.id
    try:
        db.session.commit()
        flash('Seat booked succesfully!', category='success')
    except:
        flash('An error occured while booking your seat', category='error')
    return redirect('/flight/'+str(flights))

@views.route('/flight/<int:flights>/cancel-seat/<int:id>', methods=['GET', 'POST'])
@login_required
def cancel_seat(flights, id):
    canceled_seat = Seat.query.get_or_404(id)
    canceled_seat.seat_status = 'True'
    canceled_seat.user_id = 'None'
    try:
        db.session.commit()
        flash('Seat canceled succesfully!', category='success')
    except:
        flash('An error occured while canceling your seat', category='error')
    return redirect('/flight/'+str(flights))


#@views.route('/seats', methods=['GET', 'POST'])
#@login_required
#def seats():
 #   if request.method == 'GET':
  #      with open(r'Input_Data/chartIn2.txt', 'r') as f:
   #         seat_list = []
    #        seat_list_new = []
     #       for line in f:
      #          data = line.split('\t')
       #         seat_list.append(data)
        #        for row in seat_list:
         #           row_new = []
          #          for seat in row:
           #             seat_new = seat.strip()
           #             row_new.append(seat_new)
            #    seat_list_new.append(row_new)
        #write_seats_html(seat_list_new, 'website/templates')

    #return render_template("seats.html", user=current_user)



