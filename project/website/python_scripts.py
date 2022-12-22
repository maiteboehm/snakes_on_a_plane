# document for definition of python function
import os
from datetime import date

def write_seats_html(seat_list_new, directory, filename='seats.html', cwd=os.getcwd()):
# function converts list of seat rows into html file to create seat buttons
    path_dir = os.sep.join([cwd, directory, filename])
    with open(path_dir, 'w') as file:
            file.write('{% extends "base.html" %} {% block title %}Seats{% endblock %} {% block content%} \n')
            file.write('<h1 align="center">Seats</h1> \n')
            for liste in seat_list_new:
                if liste[0] == '':
                    continue
                else:
                    file.write('<div class="container">\n')
                    for symbol in liste:
                        if liste.index(symbol) == 0: # creates row of numbers
                            file.write('\t<span class="badge badge-light col-1">' + symbol + '</span>\n')
                        #elif liste.index(symbol) == 3: # adds space for ailes
                         #   if symbol == 'X':
                          #      file.write('\t<button type="button" class="btn btn-danger btn-lg mr-3"></button>\n')
                           # else:
                            #    file.write('\t<button type="button" class="btn btn-primary btn-lg active mr-3" role="button" '
                             #      'aria-pressed="true"></button>\n')
                        elif symbol == 'X': # creates red button for already reserved seats
                            file.write('\t<button type="button" class="btn btn-danger btn-lg"></button>\n')
                        else: # creates blue responsive button for available seats
                            file.write('\t<button type="button" class="btn btn-primary btn-lg active" role="button" '
                                   'aria-pressed="true"></button>\n')
                    file.write('</div>\n')
            file.write('{% endblock %} \n') # closing endblock, has to be at the end of html document
    return

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def Column_Name_Maker(Dictionary, key):
    Column_Name_Liste = []
    for index, column_Lists in enumerate(Dictionary[str(key)]):

        if index ==0:
            Column_Name_Liste.append('Index')

        if index>0:
            Column_Name = str(column_Lists[0])
            Column_Name_Liste.append(Column_Name)

    return Column_Name_Liste
