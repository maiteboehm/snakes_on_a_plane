from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Seat
from .python_scripts import admin_user_check
from . import db
from .CharReader import Dictionary_Creater
from .CharReader import model_seat_filler
import os


admins = Blueprint('admins', __name__)

@admins.route('/', methods=['GET','POST'])
@login_required
def admin_home():
    Admin = admin_user_check(current_user)
    if Admin:
        return render_template('admin_home.html', user= current_user)


@admins.route('/user', methods=['GET', 'POST'])
@login_required
def admin_user():
    Admin = admin_user_check(current_user)
    if Admin:
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
    Admin = admin_user_check(current_user)
    if Admin:
        user_to_delete = User.query.get_or_404(id)
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
    Admin = admin_user_check(current_user)
    if Admin:
        Path = os.path.abspath(os.curdir)
        ChartIn_Path = Path +'\Input_Data\\'
        Flight_Dictionary = Dictionary_Creater(ChartIn_Path)
        model_seat_filler(Flight_Dictionary)
        return redirect('/admin-area/seats')

@admins.route('/seats', methods=['GET', 'POST'])
@login_required
def admin_seats():
    Admin = admin_user_check(current_user)
    if Admin:
        seats = Seat.query.all()
        return render_template('admin_seats.html', user=current_user, seats=seats)

@admins.route('/seats/update-seats/<int:id>', methods=['GET','POST'])
@login_required
def update_seat(id):
    Admin = admin_user_check(current_user)
    if Admin:
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
    Admin = admin_user_check(current_user)
    if Admin:
        Username = os.getlogin()
        def Database_Reader(Class):

            Occupied_Types = Class.query.filter_by(seat_status = 'False').all()
            Available_Types = Class.query.filter_by(seat_status = 'True').all()
            Number_Types = Class.query.all()
            Occupation_All_Seats = (len(Occupied_Types)*100)/len(Number_Types)
            Available_All_Seats = 100-Occupation_All_Seats
            Username = os.getlogin()
            Safeing_Directory = r'C:\Users'+'\\' + str(Username) + '\\Downloads\\'
            Name_Of_File = 'Statistics.txt'
            Filename_Dictionary = os.path.join(Safeing_Directory, Name_Of_File)


            if os.path.isfile(Filename_Dictionary) ==True:

                Output = open(Filename_Dictionary,'r')
                lines = Output.readlines()
                Version_Counter_Liste = []
                Last_Availability_Entry_Liste = []
                Last_Availability_Entry = []

                for letter in lines[0]:

                    if letter.isdigit():
                        Version_Counter_Liste.append(letter)
                        Version_Counter = ''.join(Version_Counter_Liste)

                for index,letter in enumerate(lines[int(Version_Counter)]):
                    if letter == ' ':
                        break

                    elif letter.isdigit() or '.':
                        Last_Availability_Entry.append(letter)

                Last_Availability_Entry_Liste.append(''.join(Last_Availability_Entry))

                if float(Last_Availability_Entry_Liste[0]) == float(Occupation_All_Seats):
                    print('File not updated, everything up2date')
                    return(Filename_Dictionary)

                else:
                    Output = open(Filename_Dictionary, 'a')
                    Output.write('All_Seat_Occupation All_Seat_Availability '+ str(int(Version_Counter)+1) + '\n' + str(Occupation_All_Seats) + '    ' + str(Available_All_Seats) + '\n')
                    Output.write('Occupied_Seats Available Seats' + '\n')

                    for i in range(len(Occupied_Types)):
                        Output.write(str(Occupied_Types[i]) + '    ' + str(Available_Types[i]) +  '\n')
            else:
                Output = open(Filename_Dictionary,'w')
                Version_Counter = 1
                Output.write('All_Seat_Occupation All_Seat_Availability ' + str(Version_Counter) + '\n' + str(Occupation_All_Seats) + '    ' + str(Available_All_Seats) + '\n')
                Output.write('Occupied_Seats Available Seats' + '\n')

                for i in range(len(Occupied_Types)):
                    Output.write(str(Occupied_Types[i]) + '    ' + str(Available_Types[i]) +  '\n')

            print('Ihre Datei ist unter folgendem Pfad abgelegt: ' + Safeing_Directory)

            return (Occupation_All_Seats)

        print(Database_Reader(Seat))
    return render_template('admin_statistics.html', user = current_user)

