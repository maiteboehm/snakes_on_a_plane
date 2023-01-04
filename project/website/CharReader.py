import os
import string
from .models import Seat
from . import db

Path = os.path.abspath(os.curdir)
#Project_Path = os.path.dirname(Path)
ChartIn_Path = Path + '\Input_Data\\'

def dictionary_resorter(Dictionary):

    resorted_dictionary = {

    }
    for key in Dictionary:
        temp_liste = []

        for index,row_list in enumerate(Dictionary[key]):
            temp_liste2 = []

            if index>9:
                number = str(''.join(row_list[0:2]))

            else:
                number = str(row_list[0])

            for ind,seat in enumerate(row_list):

                if seat.isdigit():
                    continue

                else:

                    seat_id = ''.join([number,seat])
                    temp_liste2.append(str(seat_id))

            temp_liste.append(temp_liste2)

        resorted_dictionary.update({key:temp_liste})

    return(resorted_dictionary)

def dictionary_creater(Filepath):
    Filename_Liste = []
#    Exception_Liste = []
    filename_dictionary = {

    }
    flight_list_number = 1

    for filename in os.listdir(Filepath):
        filename_input = []

        if filename.endswith('.txt'):
            Filename_Liste.append(filename)
            Input = open(ChartIn_Path+str(filename),mode = 'r')

            for index,line in enumerate(Input):
                line.lstrip()
                Line_Liste = []

                for letter in line:

                    if letter.isdigit():
                        continue

                    elif letter !='\t' and letter !='\n':
                        Line_Liste.append(letter)

                filename_input.append(Line_Liste)

        filename_dictionary.update({flight_list_number:filename_input})
        flight_list_number+=1
        resorted_dictionary = filename_dictionary
    return(resorted_dictionary)

def seat_identifier(Reihe):

    if len(Reihe)==10:
        aisle_list_left = ['C', 'G']
        aisle_liste_right = ['D', 'H']
        window_list = ['A', 'J']
        normal_list = ['B', 'E', 'F', 'I']

    elif len(Reihe)==8:
        aisle_list_left = ['C', 'E']
        aisle_liste_right = ['D', 'F']
        window_list = ['A', 'H']
        normal_list = ['B', 'G']

    elif len(Reihe)==6:
        aisle_list_left = ['C']
        aisle_liste_right = ['D']
        window_list = ['A', 'F']
        normal_list = ['B', 'E']

    elif len(Reihe)==4:
        aisle_list_left = ['B']
        aisle_liste_right = ['C']
        window_list = ['A', 'D']
        normal_list = []

    return(aisle_list_left,aisle_liste_right,window_list,normal_list)
def model_seat_filler(Dictionary):
    alphabet = list(string.ascii_uppercase)
    flight_list = []
    seat_row_list = []
    seat_type_list = []
    seat_column_list = []
    seat_status = []

    for key, value in Dictionary.items():

        for ind,row in enumerate(value):

            typen_listen = seat_identifier(row)

            for number_seat,column in enumerate(row):
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
            new_flight_list = Seat(flight_list = flight_list[i], seat_row = seat_row_list[i], seat_column = seat_column_list[i],
                              seat_status = seat_status[i], seat_type = seat_type_list[i], seat_unique = seat_unique)
            db.session.add(new_flight_list)

    db.session.commit()
    #print(len(flight_list),len(seat_column_list),len(seat_row_list),len(seat_status))
    return (flight_list,seat_row_list,seat_column_list,seat_status,seat_type_list)
#Resorted_Dictionary = Dictionary_Creater(ChartIn_Path)
#print(model_seat_filler(Resorted_Dictionary))

