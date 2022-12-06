from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from os import path
from datetime import date


db = SQLAlchemy()
DB_NAME = "database.db"



def create_app():
    from .views import views
    from .auth import auth
    from .models import User
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    db.init_app(app)
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    class MyAdminView(AdminIndexView):
        def is_accessible(self):
            if current_user.is_authenticated == True:
                if current_user.role == 'admin':
                    return current_user.is_authenticated
                else:
                    current_user.is_authenticated = False
                    return current_user.is_authenticated
        def inaccessible_callback(self, name, **kwargs):
            return redirect(url_for('views.home'))
        column_exclude_list = ['password']

    admin = Admin(app, name='Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
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


