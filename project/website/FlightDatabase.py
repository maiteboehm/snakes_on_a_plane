from flask import Flask
from python_scripts import Column_Name_Maker
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
db.init_app(app)
with app.app_context():
    db.create_all()

#introduction of the database class
class Flieger(db.Model):

    #create tables for the database with id Column for each table
    for key, value in Test_Dictionary.items():
        __tablename__ = str(key)

        Column_Name_Liste = Column_Name_Maker(Test_Dictionary,key)
        id = db.Column(db.Integer, primary_key=True)

        for name in Column_Name_Liste:
            exec(f'{name} = db.Column(db.String(2), nullable = False)')

db.create_all()





