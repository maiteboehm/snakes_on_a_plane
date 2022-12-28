import string

from flask import Flask
from python_scripts import Column_Name_Maker
from flask_sqlalchemy import SQLAlchemy
from CharReader import Resorted_Dictionary
from CharReader import Test_Dictionary
alphabet = list(string.ascii_uppercase)
#print(alphabet[0:13])
Flight = []
Seat_row_liste = []
Seat_type = []
Seat_liste = []
Seat_status = []
index = 1
print(alphabet[4:13])
for key, value in Resorted_Dictionary.items():
    #print(key,value[1:])
    for ind,Row in enumerate(value[1:]):
        for Seat in Row:
            Seat_row_liste.append(ind + 1)
            #print(Seat,index,Row)
            Flight.append(index)
            Seat_liste.append(Seat)
        for letter in str(Row):
            if letter =='X':
                Seat_type.append('Vergeben')
                #letter = str(Row[])
                Seat_status.append(False)
            elif letter in alphabet[0:13]:
                Seat_status.append(True)
            if letter == 'A':
                Seat_type.append('Fenster')
                #print(letter)
            elif letter == 'B':
                Seat_type.append('Fenster')
            elif letter == 'C':
                Seat_type.append('Gang')
            elif letter == 'D':
                #print(letter)
                Seat_type.append('Gang')
            elif letter in alphabet[4:13]:
                #print(letter)
                Seat_type.append('Normal')

    index+=1
for index,value in enumerate(Seat_type):
    print(Flight[index],value,Seat_liste[index],)
#print(Flight,Seat_status,Seat_liste,Seat_type,Seat_row_liste)
print(len(Flight),len(Seat_status),len(Seat_liste),len(Seat_type),len(Seat_row_liste))
#db.session.add(new_flight)
#db.session.commit()
