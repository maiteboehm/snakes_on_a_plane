import string
from CharReader import Resorted_Dictionary

def model_seat_filler(Dictionary):
    alphabet = list(string.ascii_uppercase)
    Flight = []
    Seat_row_liste = []
    Seat_type = []
    Seat_liste = []
    Seat_status = []
    #print(alphabet[4:13])
    for key, value in Dictionary.items():

        for ind,Row in enumerate(value[1:]):
            print(Row,len(Row))
            for Number_Seat,Seat in enumerate(Row):
                Seat_row_liste.append(ind + 1)
                Flight.append(key)
                Seat_liste.append(Seat)

                for letter in str(Seat):
                    if letter == 'X':
                        letter = alphabet[Number_Seat]
                        Seat_status.append(False)

                    elif letter in alphabet[0:13]:
                        Seat_status.append(True)

                    if letter == 'A' or letter == 'B':
                        Seat_type.append('Fenster')

                    elif letter == 'C' or letter == 'D':
                        Seat_type.append('Gang')

                    elif letter in alphabet[4:13]:
                        Seat_type.append('Normal')


    #for i in range(len(Flight)):
        #New_flight = Seat(flight = Flight[i], seat_row = Seat_row_liste[i], seat_column = Seat_liste[i], seat_status = Seat_status[i], seat_type = Seat_type[i])
        #db.session.add(New_flight)

    #db.session.commit()
    #print(len(Flight),len(Seat_row_liste))
    return (Flight,Seat_row_liste,Seat_liste,Seat_status,Seat_type)
print(model_seat_filler(Resorted_Dictionary))