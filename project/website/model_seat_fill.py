import string
from .models import Seat
from . import db
#from CharReader import Resorted_Dictionary
def Seat_Identifier(Reihe):

    if len(Reihe)==10:
        Gang_Liste_Links = ['C','G']
        Gang_Liste_Rechts = ['D','H']
        Fenster_Liste = ['A','J']
        Normal_Liste = ['B','E','F','I']

    elif len(Reihe)==8:
        Gang_Liste_Links = ['C', 'E']
        Gang_Liste_Rechts = ['D','F']
        Fenster_Liste = ['A', 'H']
        Normal_Liste = ['B', 'G']

    elif len(Reihe)==6:
        Gang_Liste_Links = ['C']
        Gang_Liste_Rechts = ['D']
        Fenster_Liste = ['A','F']
        Normal_Liste = ['B', 'E']

    elif len(Reihe)==4:
        Gang_Liste_Links = ['B']
        Gang_Liste_Rechts = ['C']
        Fenster_Liste = ['A','D']
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

        for ind,row in enumerate(value[1:]):
            Typen_Listen = Seat_Identifier(row)

            for number_seat,column in enumerate(row):
                Seat_Row_Liste.append(ind + 1)
                Flight.append(key)

                for letter in str(column):

                    if letter == 'X':
                        letter = Alphabet[number_seat]
                        Replaced_Seat =''.join([letter])
                        Seat_Column_Liste.append(Replaced_Seat)
                        Seat_Status.append('False')
                    elif letter in Alphabet[0:13]:
                        Seat_Status.append('True')
                        Seat_Column_Liste.append(''.join([letter]))

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
#print(model_seat_filler(Resorted_Dictionary))
