from flask import Flask, Blueprint, render_template, request
from flask_login import login_required, current_user
import os

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/seats', methods=['GET', 'POST'])
def seats():
    if request.method == 'GET':
        cwd = os.getcwd()
        directory1 = 'website'
        directory2 = 'templates'
        filename = 'seats.html'
        path_dir = os.sep.join([cwd, directory1, directory2, filename])
        with open(r'Input_Data/chartIn4.txt', 'r') as f:
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
        with open(path_dir, 'w') as file:
            file.write('{% extends "base.html" %} {% block title %}Seats{% endblock %} {% block content%} \n')
            file.write('<h1 align="center">Seats</h1> \n')
            for liste in seat_list_new:
                file.write('<div>\n')
                for symbol in liste:
                    if symbol == ' ':
                        file.write()
                    else:
                        file.write('\t<button type="button">' + symbol + '</button>\n')
                file.write('</div>\n')
            file.write('{% endblock %} \n') # closing endblock, has to be at the end of html document

    return render_template("seats.html", user=current_user)



