import os
import string
from .models import Seat
from . import db

Path = os.path.abspath(os.curdir)
# Project_Path = os.path.dirname(Path)
ChartIn_Path = Path + r'\Input_Data\\'


def dictionary_creater(filepath):
    """ Creates dictionary from text files in filepath with the function argument being the filepath of files.
    Returns dictionary with flight number as key and list of rows of the specific flight(list of of lists) as value.
    """
    filename_liste = []
    filename_dictionary = {

    }
    flight_list_number = 1
    for filename in os.listdir(filepath):
        filename_input = []

        if filename.endswith('.txt'):
            filename_liste.append(filename)
            input = open(filepath+str(filename), mode='r')

            for index, line in enumerate(input):
                line.lstrip()
                line_liste = []

                for letter in line:

                    if letter.isdigit():
                        continue

                    elif letter != '\t' and letter != '\n':
                        line_liste.append(letter)

                tmp_list = []

                if line[0] == '1' and index == 0:
                    alphabet = list(string.ascii_uppercase)

                    for i in range(len(line_liste)):

                        tmp_list.append(alphabet[i])
                    filename_input.append(tmp_list)

                filename_input.append(line_liste)

        filename_dictionary.update({flight_list_number: filename_input[1:]})
        flight_list_number += 1
        resorted_dictionary = filename_dictionary
    return resorted_dictionary

# print(dictionary_creater(ChartIn_Path))


def seat_identifier(reihe):
    """Seat_Identifier serves as Function to define the different types of seats that are present in the Flight.
    The Function takes a row as argument and returns lists that contain the seats in capital letters according to their
    type.
    """
    if len(reihe) == 10:
        aisle_list_left = ['C', 'G']
        aisle_liste_right = ['D', 'H']
        window_list = ['A', 'J']
        normal_list = ['B', 'E', 'F', 'I']

    elif len(reihe) == 8:
        aisle_list_left = ['C', 'E']
        aisle_liste_right = ['D', 'F']
        window_list = ['A', 'H']
        normal_list = ['B', 'G']

    elif len(reihe) == 6:
        aisle_list_left = ['C']
        aisle_liste_right = ['D']
        window_list = ['A', 'F']
        normal_list = ['B', 'E']

    elif len(reihe) == 4:
        aisle_list_left = ['B']
        aisle_liste_right = ['C']
        window_list = ['A', 'D']
        normal_list = []

    return aisle_list_left, aisle_liste_right, window_list, normal_list


def model_seat_filler(Dictionary):
    """Function takes the Dictionary as argument and fills the class seat of the Database which is initialized in
    __init__ with values from the Dictionary. Returns the Lists which are filled in the Database.
    """
    alphabet = list(string.ascii_uppercase)
    flight_list = []
    seat_row_list = []
    seat_type_list = []
    seat_column_list = []
    seat_status = []

    for key, value in Dictionary.items():

        for ind, row in enumerate(value):

            type_list = seat_identifier(row)

            for number_seat, column in enumerate(row):
                seat_row_list.append(ind + 1)
                flight_list.append(key)

                for letter in str(column):

                    if letter == 'X':
                        letter = alphabet[number_seat]
                        replaced_seat = letter
                        seat_column_list.append(replaced_seat)
                        seat_status.append('False')

                    elif letter in alphabet[0:13]:
                        seat_status.append('True')
                        seat_column_list.append(letter)

                    if letter in type_list[0]:
                        seat_type_list.append('Aisle_Left')

                    elif letter in type_list[1]:
                        seat_type_list.append('Aisle_Right')

                    elif letter in type_list[2]:
                        seat_type_list.append('Window')

                    elif letter in type_list[3]:
                        seat_type_list.append('Normal')

    for i in range(len(flight_list)):
        seat_unique = str(flight_list[i])+'_'+str(seat_row_list[i])+'_'+str(seat_column_list[i])
        seat_unique_check = Seat.query.filter_by(seat_unique=seat_unique).first()
        if seat_unique_check:
            continue
        else:
            new_flight_list = Seat(seat_flight=flight_list[i], seat_row=seat_row_list[i],
                                   seat_column=seat_column_list[i], seat_status=seat_status[i], 
                                   seat_type=seat_type_list[i], seat_unique=seat_unique)
            db.session.add(new_flight_list)

    db.session.commit()

    return flight_list, seat_row_list, seat_column_list, seat_status, seat_type_list
