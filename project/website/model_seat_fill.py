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
    alphabet = list(string.ascii_uppercase)
    Flight = []
    Seat_row_liste = []
    Seat_type = []
    Seat_column_liste = []
    Seat_status = []
    #print(alphabet[4:13])
    for key, value in Dictionary.items():

        for ind,Row in enumerate(value[1:]):
            print(Row,len(Row))
            Typen_Listen = Seat_Identifier(Row)

            for Number_Seat,column in enumerate(Row):
                Seat_row_liste.append(ind + 1)
                Flight.append(key)
                Seat_column_liste.append(column)

                for letter in str(column):
                    print(Typen_Listen)
                    if letter == 'X':
                        letter = alphabet[Number_Seat]
                        Seat_status.append('False')

                    if letter in Typen_Listen[0]:
                        Seat_type.append('Gang')
                        print(Typen_Listen[0],'Gang')
                    elif letter in Typen_Listen[1]:
                        print(Typen_Listen[1],'Fenster')
                        Seat_type.append('Fenster')

                    elif letter in Typen_Listen[2]:
                        Seat_type.append('Normal')
                        print(Typen_Listen[2],'Normal')

    for i in range(len(Flight)):
        New_flight = Seat(flight = Flight[i], seat_row = Seat_row_liste[i], seat_column = Seat_liste[i], seat_status = Seat_status[i], seat_type = Seat_type[i])
        db.session.add(New_flight)

    for i in range(len(Flight)):
        New_flight = Seat(flight = Flight[i], seat_row = Seat_row_liste[i], seat_column = Seat_column_liste[i], seat_status = Seat_status[i], seat_type = Seat_type[i])
        db.session.add(New_flight)

    db.session.commit()
    return (Flight,Seat_row_liste,Seat_column_liste,Seat_status,Seat_type)

    db.session.commit()
    #print(len(Flight),len(Seat_row_liste),len(Seat_type))
    #print(Seat_type)
    return (Flight,Seat_row_liste,Seat_liste,Seat_status,Seat_type)
