import os
import string
from .models import Seat
from . import db

Path = os.path.abspath(os.curdir)
# Project_Path = os.path.dirname(Path)
ChartIn_Path = Path + r'\Input_Data\\'


def dictionary_resorter(dictionary):

    resorted_dictionary = {

    }
    for key in dictionary:
        temp_list = []

        for index, row_list in enumerate(dictionary[key]):
            temp_list2 = []

            if index > 9:
                number = str(''.join(row_list[0:2]))

            else:
                number = str(row_list[0])

            for ind, seat in enumerate(row_list):

                if seat.isdigit():
                    continue

                else:

                    seat_id = ''.join([number, seat])
                    temp_list2.append(str(seat_id))

            temp_list.append(temp_list2)

        resorted_dictionary.update({key: temp_list})

    return resorted_dictionary


def dictionary_creater(filepath):
    filename_liste = []
#    Exception_Liste = []
    filename_dictionary = {

    }
    flight_list_number = 1

    for filename in os.listdir(filepath):
        filename_input = []

        if filename.endswith('.txt'):
            filename_liste.append(filename)
            input = open(ChartIn_Path+str(filename), mode='r')

            for index, line in enumerate(input):
                line.lstrip()
                line_liste = []

                for letter in line:

                    if letter.isdigit():
                        continue

                    elif letter != '\t' and letter != '\n':
                        line_liste.append(letter)

                filename_input.append(line_liste)

        filename_dictionary.update({flight_list_number: filename_input})
        flight_list_number += 1
        resorted_dictionary = filename_dictionary
    return resorted_dictionary


def seat_identifier(reihe):

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
    alphabet = list(string.ascii_uppercase)
    flight_list = []
    seat_row_list = []
    seat_type_list = []
    seat_column_list = []
    seat_status = []

    for key, value in Dictionary.items():

        for ind, row in enumerate(value):

            typen_listen = seat_identifier(row)

            for number_seat, column in enumerate(row):
                seat_row_list.append(ind + 1)
                flight_list.append(key)

                for letter in str(column):

                    if letter == 'X':
                        letter = alphabet[number_seat]
                        Replaced_Seat = letter
                        seat_column_list.append(Replaced_Seat)
                        seat_status.append('False')

                    elif letter in alphabet[0:13]:
                        seat_status.append('True')
                        seat_column_list.append(letter)

                    if letter in typen_listen[0]:
                        seat_type_list.append('Aisle_Left')

                    elif letter in typen_listen[1]:
                        seat_type_list.append('Aisle_Right')

                    elif letter in typen_listen[2]:
                        seat_type_list.append('Window')

                    elif letter in typen_listen[3]:
                        seat_type_list.append('Normal')

    for i in range(len(flight_list)):
        seat_unique = str(flight_list[i])+'_'+str(seat_row_list[i])+'_'+str(seat_column_list[i])
        seat_unique_check = Seat.query.filter_by(seat_unique=seat_unique).first()
        if seat_unique_check:
            continue
        else:
            new_flight_list = Seat(flight_list=flight_list[i], seat_row=seat_row_list[i], 
                                   seat_column=seat_column_list[i], seat_status=seat_status[i], 
                                   seat_type=seat_type_list[i], seat_unique=seat_unique)
            db.session.add(new_flight_list)

    db.session.commit()
# print(len(flight_list),len(seat_column_list),len(seat_row_list),len(seat_status))
    return flight_list, seat_row_list, seat_column_list, seat_status, seat_type_list

# Resorted_Dictionary = Dictionary_Creater(ChartIn_Path)
# print(model_seat_filler(Resorted_Dictionary))
