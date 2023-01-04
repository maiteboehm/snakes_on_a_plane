import os
import string
from .models import Seat
from . import db

Path = os.path.abspath(os.curdir)
#Project_Path = os.path.dirname(Path)
ChartIn_Path = Path +'\Input_Data\\'

def Dictionary_Resorter(Dictionary):

    Resorted_Dictionary = {

    }
    for key in Dictionary:
        Temp_Liste = []

        for index,row_list in enumerate(Dictionary[key]):
            Temp_Liste2 = []

            if index>9:
                Number = str(''.join(row_list[0:2]))

            else:
                Number = str(row_list[0])

            for ind,seat in enumerate(row_list):

                if seat.isdigit():
                    continue

                else:

                    Seat_ID = ''.join([Number,seat])
                    Temp_Liste2.append(str(Seat_ID))

            Temp_Liste.append(Temp_Liste2)

        Resorted_Dictionary.update({key:Temp_Liste})

    return(Resorted_Dictionary)

def Dictionary_Creater(Filepath):
    Filename_Liste = []
#    Exception_Liste = []
    Filename_Dictionary = {

    }
    Flight_Number = 1

    for filename in os.listdir(Filepath):
        Filename_Input = []

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

                Filename_Input.append(Line_Liste)

        Filename_Dictionary.update({Flight_Number:Filename_Input})
        Flight_Number+=1
        Resorted_Dictionary = Filename_Dictionary
    return(Resorted_Dictionary)

def Seat_Identifier(Reihe):

    if len(Reihe)==10:
        Gang_Liste_Links = ['C', 'G']
        Gang_Liste_Rechts = ['D', 'H']
        Fenster_Liste = ['A', 'J']
        Normal_Liste = ['B', 'E', 'F', 'I']

    elif len(Reihe)==8:
        Gang_Liste_Links = ['C', 'E']
        Gang_Liste_Rechts = ['D', 'F']
        Fenster_Liste = ['A', 'H']
        Normal_Liste = ['B', 'G']

    elif len(Reihe)==6:
        Gang_Liste_Links = ['C']
        Gang_Liste_Rechts = ['D']
        Fenster_Liste = ['A', 'F']
        Normal_Liste = ['B', 'E']

    elif len(Reihe)==4:
        Gang_Liste_Links = ['B']
        Gang_Liste_Rechts = ['C']
        Fenster_Liste = ['A', 'D']
        Normal_Liste = []

    return(Gang_Liste_Links,Gang_Liste_Rechts,Fenster_Liste,Normal_Liste)
def model_seat_filler(Dictionary):
    Alphabet = list(string.ascii_uppercase)
    Flight = []
    Seat_Row_Liste = []
    Seat_Type = []
    Seat_Column_Liste = []
    Seat_Status = []

    for key, value in Dictionary.items():

        for ind,row in enumerate(value):

            Typen_Listen = Seat_Identifier(row)

            for number_seat,column in enumerate(row):
                Seat_Row_Liste.append(ind + 1)
                Flight.append(key)

                for letter in str(column):

                    if letter == 'X':
                        letter = Alphabet[number_seat]
                        Replaced_Seat = letter
                        Seat_Column_Liste.append(Replaced_Seat)
                        Seat_Status.append('False')

                    elif letter in Alphabet[0:13]:
                        Seat_Status.append('True')
                        Seat_Column_Liste.append(letter)

                    if letter in Typen_Listen[0]:
                        Seat_Type.append('Aisle_Left')

                    elif letter in Typen_Listen[1]:
                        Seat_Type.append('Aisle_Right')

                    elif letter in Typen_Listen[2]:
                        Seat_Type.append('Window')

                    elif letter in Typen_Listen[3]:
                        Seat_Type.append('Normal')

    for i in range(len(Flight)):
        Seat_Unique = str(Flight[i])+'_'+str(Seat_Row_Liste[i])+'_'+str(Seat_Column_Liste[i])
        Seat_Unique_Check = Seat.query.filter_by(seat_unique=Seat_Unique).first()
        if Seat_Unique_Check:
            continue
        else:
            New_Flight = Seat(flight = Flight[i], seat_row = Seat_Row_Liste[i], seat_column = Seat_Column_Liste[i],
                              seat_status = Seat_Status[i], seat_type = Seat_Type[i], seat_unique = Seat_Unique)
            db.session.add(New_Flight)

    db.session.commit()
    #print(len(Flight),len(Seat_Column_Liste),len(Seat_Row_Liste),len(Seat_Status))
    return (Flight,Seat_Row_Liste,Seat_Column_Liste,Seat_Status,Seat_Type)
#Resorted_Dictionary = Dictionary_Creater(ChartIn_Path)
#print(model_seat_filler(Resorted_Dictionary))

