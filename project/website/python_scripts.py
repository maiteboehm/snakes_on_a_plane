# document for definition of python function
import os

def write_seats_html(seat_list_new, directory, filename='seats.html', cwd=os.getcwd()):
# function converts list of seat rows into html file to create seat buttons
    path_dir = os.sep.join([cwd, directory, filename])
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
    return
