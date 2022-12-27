from flask import Flask
from python_scripts import Column_Name_Maker
from flask_sqlalchemy import SQLAlchemy
from CharReader import Resorted_Dictionary

for key, value in Resorted_Dictionary.items():
    print(key,value[1:])

