from flask import Flask

from flask_sqlalchemy import SQLAlchemy
#from CharReader import Filename_Liste

Test_Dictionary = {
'Filename':[[1,2],['A','A'],['B','B'],['C','C'],['D','D']],
'Filename2':[[1,2],['A','A'],['B','B'],['C','C']]
}

DB_NAME = "Flieger.db"
#create Flask Instance
app = Flask(__name__)
DB_NAME = "Flieger.db" #name of Database
#add Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

#initialize the Database
db = SQLAlchemy(app)


#makes names for the columns of the tables:
def Column_Name_Maker(Dictionary, key):
    Column_Name_Liste = []
    for index, column_Lists in enumerate(Dictionary[str(key)]):

        if index ==0:
            Column_Name_Liste.append('Index')

        if index>0:
            Column_Name = str(column_Lists[0])
            Column_Name_Liste.append(Column_Name)

    return Column_Name_Liste
#introduction of the database class
class Flieger(db.Model):

    #create tables for the database with id Column for each table
    for key, value in Test_Dictionary.items():
        __tablename__ = str(key)

        Column_Name_Liste = Column_Name_Maker(Test_Dictionary,key)
        id = db.Column(db.Integer, primary_key=True)

        for name in Column_Name_Liste:
            exec(f'{name} = db.Column(db.String(2), nullable = False)')

#            for index, column in enumerate(Test_Dictionary[str(key)]):
#                #print(column)
#
#                if index == 0:
#                    Index = db.Column(db.Integer(1))
#                else:
#
#                    for i in range(len(Column_Name_Liste)):
#                        Column_Name_Liste[i] = db.Column(db.String(2))
        # not sure how to utilize the __init__ function for the db_database.




for key, item in Test_Dictionary.items():
    for index,column in enumerate(item):
        if index==0:
            print('True',column)


    #for seats in column_Lists:
    #    print(seats)
#print(Column_Name)



