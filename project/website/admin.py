from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Seat
from .python_scripts import admin_user_checker
from . import db
from .CharReader import dictionary_creater
from .CharReader import model_seat_filler
import os


admins = Blueprint('admins', __name__)


@admins.route('/', methods=['GET'])
@login_required
def admin_home():
    """Creates the home page of the admin-area."""
    admin = admin_user_checker(current_user)
    if admin:
        return render_template('admin_home.html', user=current_user)


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


@admins.route('user/delete-user/<int:id>', methods=['POST', 'GET'])
@login_required
def delete_user(id):
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


@admins.route('/update-flights', methods=['GET', 'POST'])
@login_required
def admin_flights():
    admin = admin_user_checker(current_user)
    if admin:
        path = os.path.abspath(os.curdir)
        chart_in_path = path + r'\Input_Data\\'
        flight_dictionary = dictionary_creater(chart_in_path)
        model_seat_filler(flight_dictionary)
        return redirect('/admin-area/seats')


@admins.route('/seats', methods=['GET', 'POST'])
@login_required
def admin_seats():
    admin = admin_user_checker(current_user)
    if admin:
        seats = Seat.query.all()
        return render_template('admin_seats.html', user=current_user, seats=seats)


@admins.route('/seats/update-seats/<int:id>', methods=['GET', 'POST'])
@login_required
def update_seat(id):
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


@admins.route('/statistics', methods=['GET', 'POST'])
@login_required
def admin_statistics():
    admin = admin_user_checker(current_user)
    if admin:
        # Username = os.getlogin()

        """Reads the Database which contains the Seat_IDs(Int,prim.key), Flight_Numbers(int), Seats(Capital Letters), 
        Seat_types (defined by the seat_identifier function in Charreader) and Occupation_status(True or False Str)
        and evaluates how many seats are occupied or available and saves them to the Statistics.txt in the Output_Data 
        Directory of the project."""
        def database_reader(class_variable):
            occupied_types = class_variable.query.filter_by(seat_status='False').all()
            available_types = class_variable.query.filter_by(seat_status='True').all()
            number_types = class_variable.query.all()
            occupation_all_seats = (len(occupied_types) * 100) / len(number_types)
            available_all_seats = 100 - occupation_all_seats
            username = os.getlogin()
            saving_directory = r'C:\Users' + '\\' + str(username) + '\\Downloads\\'
            name_of_file = 'Statistics.txt'
            filename_dictionary = os.path.join(saving_directory, name_of_file)
            if os.path.isfile(filename_dictionary):
                output = open(filename_dictionary, 'r')
                lines = output.readlines()
                version_counter_liste = []
                last_availability_entry_liste = []
                last_availability_entry = []

                for letter in lines[0]:

                    if letter.isdigit():
                        version_counter_liste.append(letter)
                        version_counter = ''.join(version_counter_liste)

                for index,letter in enumerate(lines[int(version_counter)]):
                    if letter == ' ':
                        break

                    elif letter.isdigit() or '.':
                        last_availability_entry.append(letter)

                last_availability_entry_liste.append(''.join(last_availability_entry))

                if float(last_availability_entry_liste[0]) == float(occupation_all_seats):
                    print('File not updated, everything up2date')
                    return(filename_dictionary)

                else:
                    output = open(filename_dictionary, 'a')
                    output.write('All_Seat_Occupation All_Seat_Availability ' + str(int(version_counter) + 1) + '\n' + str(occupation_all_seats) + '    ' + str(available_all_seats) + '\n')
                    output.write('Occupied_Seats Available Seats' + '\n')

                    for i in range(len(occupied_types)):
                        output.write(str(occupied_types[i]) + '    ' + str(available_types[i]) + '\n')
            else:
                output = open(filename_dictionary, 'w')
                version_counter = 1
                output.write('All_Seat_Occupation All_Seat_Availability ' + str(version_counter) + '\n' + str(occupation_all_seats) + '    ' + str(available_all_seats) + '\n')
                output.write('Occupied_Seats Available Seats' + '\n')

                for i in range(len(occupied_types)):
                    output.write(str(occupied_types[i]) + '    ' + str(available_types[i]) + '\n')

            print('Ihre Datei ist unter folgendem Pfad abgelegt: ' + saving_directory)

            return (occupation_all_seats)

        print(database_reader(Seat))
    return render_template('admin_statistics.html', user = current_user)

