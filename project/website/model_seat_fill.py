import string
from . import db
from flask_login import UserMixin
from models import Seat
from flask import Flask
from python_scripts import Column_Name_Maker
from flask_sqlalchemy import SQLAlchemy
from CharReader import Resorted_Dictionary
from CharReader import Test_Dictionary
#print(Test_Dictionary)
alphabet = list(string.ascii_uppercase)
#print(alphabet[0:13])
Flight = []
Seat_row_liste = []
Seat_type = []
Seat_liste = []
Seat_status = []
index = 1
#print(alphabet[4:13])
for key, value in Resorted_Dictionary.items():
    #print(value[0])
    #print(key,value[1:])
    for ind,Row in enumerate(value[1:]):
        for Number_Seat,Seat in enumerate(Row):
            Seat_row_liste.append(ind + 1)
            Flight.append(index)
            Seat_liste.append(Seat)
            #print(Number_Seat,Seat)
            for letter in str(Seat):
                #print(letter)
                if letter == 'X':
                    #print(letter,ind,Number_Seat)
                    letter = alphabet[Number_Seat]
                    #print(letter)
                    Seat_status.append(False)

                elif letter in alphabet[0:13]:
                    Seat_status.append(True)

                if letter == 'A' or letter == 'B':
                    Seat_type.append('Fenster')

                elif letter == 'C' or letter == 'D':
                    Seat_type.append('Gang')

                elif letter in alphabet[4:13]:
                    Seat_type.append('Normal')

    index+=1
#for index,value in enumerate(Seat_type):
    #print(Flight[index],value,Seat_liste[index],)
#print(Flight,Seat_status,Seat_liste,Seat_type,Seat_row_liste)
new_flight = Seat(flight = Flight, seat_row = Seat_row_liste, seat_column = Seat_Liste, seat_status = Seat_status, seat_type = Seat_Type)
print(len(Flight),len(Seat_status),len(Seat_liste),len(Seat_type),len(Seat_row_liste))

db.session.add(new_flight)
db.session.commit()
