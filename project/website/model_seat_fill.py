import string
from .models import Seat
from . import db
#from CharReader import Resorted_Dictionary
def Seat_Identifier(Reihe):

    if len(Reihe)==10:
        Gang_Liste = ['C','D','F','G']
        Fenster_Liste = ['A','J']
        Normal_Liste = ['B','E','H','I']

    elif len(Reihe)==6:
        Gang_Liste = ['C','D']
        Fenster_Liste = ['A','F']
        Normal_Liste = ['B', 'E']

    elif len(Reihe)==4:
        Gang_Liste = ['A','D']
        Fenster_Liste = ['B','C']
        Normal_Liste = []

    return(Gang_Liste,Fenster_Liste,Normal_Liste)

def model_seat_filler(Dictionary):
    Alphabet = list(string.ascii_uppercase)
    Flight = []
    Seat_Row_Liste = []
    Seat_Type = []
    Seat_Column_Liste = []
    Seat_Status = []

    for key, value in Dictionary.items():

        for ind,row in enumerate(value[1:]):
            Typen_Listen = Seat_Identifier(row)

            for number_seat,column in enumerate(row):
                Seat_Row_Liste.append(ind + 1)
                Flight.append(key)

                for letter in str(column):

                    if letter == 'X':
                        letter = Alphabet[number_seat]
                        Replaced_Seat =''.join([str(ind+1),letter])
                        Seat_Column_Liste.append(Replaced_Seat)
                        Seat_Status.append('False')

                    elif letter in Alphabet[0:13]:
                        Seat_Status.append('True')
                        Seat_Column_Liste.append(''.join([str(ind+1), letter]))

                    if letter in Typen_Listen[0]:
                        Seat_Type.append('Gang')

                    elif letter in Typen_Listen[1]:
                        Seat_Type.append('Fenster')

                    elif letter in Typen_Listen[2]:
                        Seat_Type.append('Normal')

    for i in range(len(Flight)):

        New_Flight = Seat(flight = Flight[i], seat_row = Seat_Row_Liste[i], seat_column = Seat_Column_Liste[i], seat_status = Seat_Status[i], seat_type = Seat_Type[i])
        db.session.add(New_Flight)

    db.session.commit()
    #print(len(Flight),len(Seat_Column_Liste),len(Seat_Row_Liste),len(Seat_Status))
    return (Flight,Seat_Row_Liste,Seat_Column_Liste,Seat_Status,Seat_Type)
#print(model_seat_filler(Resorted_Dictionary))