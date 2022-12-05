from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from os import path
from datetime import date


db = SQLAlchemy()
DB_NAME = "database.db"



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User

    class MyModelView(ModelView):
        column_exclude_list = ['password']

    admin = Admin(app, name='Admin', template_mode='bootstrap3')
    admin.add_view(MyModelView(User, db.session))

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
        db.init_app(app)
        with app.app_context():
            db.create_all()
    return app

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


