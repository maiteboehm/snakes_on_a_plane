from flask import Flask, redirect, url_for, flash
import flask_sqlalchemy
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
#from CharReader import Filename_Liste
DB_NAME = "Flieger.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{DB_Name}'

db = SQLAlchemy(app)


Test_Dictionary = {
'Filename':[[1,2],['A','A'],['B','B'],['C','C']],
'Filename2':[[1,2],['A','A'],['B','B'],['C','C']]
}
#makes names for the columns of the tables:
def Column_Name_Maker(Dictionary, key):
    Column_Name_Liste = []
    for index, column_Lists in enumerate(Dictionary[str(key)]):
        #print(column_Lists[0])
        if index>0:
            Column_Name = str(column_Lists[0])
            Column_Name_Liste.append(Column_Name)
    return Column_Name_Liste
#introduction of the database class
    class Flieger(db.Model):

        for key, value in Test_Dictionary.items():
            print(key,value)
            __tablename__ = str(key)
            id = db.Column(db.Integer, primary_key = True)
            Column_Name_Liste = Column_Name_Maker(Test_Dictionary,key)

            for index, column in enumerate(Test_Dictionary[str(key)]):
                print(column)

                if index == 0:
                    Index = db.Column(db.Integer(1))
                else:

                    for i in range(len(Column_Name_Liste)):
                        Column_Name_Liste[i] = db.Column(db.String(2))
        # not sure how to utilize the __init__ function for the db_database.
        def __init__(self, ):
            self.Index = Index
            #creates columns for the specific column names which are given by the name list.
            for name in Column_Name_Liste:
                exec(f'{name} = Column(String')

Column_Name_Liste = Column_Name_Maker(Test_Dictionary,'Filename')
print(Column_Name_Liste)



for key, item in Test_Dictionary.items():
    for index,column in enumerate(item):
        if index==0:
            print('True',column)


    #for seats in column_Lists:
    #    print(seats)
#print(Column_Name)



