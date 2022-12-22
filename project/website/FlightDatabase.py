from flask import Flask, redirect, url_for, flash
import flask_sqlalchemy
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from CharReader import Filename_Liste
DB_NAME = "Flieger.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{DB_Name}'

db = SQLAlchemy(app)


Test_Dictionary = {
'Filename':[[1,2],['A','A'],['B','B'],['C','C']],
'Filename2':[[1,2],['A','A'],['B','B'],['C','C']]
}
#makes names for the columns of the subclasses:
def Column_Name_Maker(Dictionary,key):
    Column_Name_Liste = []
    for column_Lists in Dictionary[str(key)]:
        print(column_Lists[0])
        Column_Name = str(column_Lists[0])
        Column_Name_Liste.append(Column_Name)
    return Column_Name_Liste

    class Flieger(db.Model):
        for key, value in Test_Dictionary.items():
            print(key)
            __tablename__ = str(key)
            id = db.Column(db.Integer, primary_key = True)
            for column in Test_Dictionary[str(key)]:
                print(column)

        #for column_name in Column_Name_Maker(Test_Dictionary,key):
        #    setattr(Flieger, column_name, Column(String))



for key, item in Test_Dictionary.items():
    print(Column_Name_Maker(Test_Dictionary,key))


    #for seats in column_Lists:
    #    print(seats)
#print(Column_Name)
#Klasse der neuen Tabellen in der Parentclass Fliegertypen



