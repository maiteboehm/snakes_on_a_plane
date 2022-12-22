import flask_sqlalchemy
import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from CharReader import Filename_Liste

Fliegertypen = declarative_base()

Test_Dictionary = {
'Filename':[['A','A'],['B','B'],['C','C']],
'Filename2':[['A','A'],['B','B'],['C','C']]
}
#makes names for the columns of the subclasses:
def Column_Name_Maker(Dictionary,key):
    Column_Name_Liste = []
    for column_Lists in Dictionary[str(key)]:
        print(column_Lists[0])
        Column_Name = str(column_Lists[0])
        Column_Name_Liste.append(Column_Name)
    return Column_Name_Liste

for key,value in Test_Dictionary.items():
    class Flieger(Fliegertypen):
        def __init__(self, name):
            self.__tablename__ = __tablename__
            self.__tablename__ = str(key)
        id = Column(Integer, primary_key = True, nullable = False)
        for column_name in Column_Name_Maker(Test_Dictionary,key):
            setattr(Flieger, column_name, Column(String))


for key, item in Test_Dictionary.items():
    print(Column_Name_Maker(Test_Dictionary,key))


    #for seats in column_Lists:
    #    print(seats)
#print(Column_Name)
#Klasse der neuen Tabellen in der Parentclass Fliegertypen



