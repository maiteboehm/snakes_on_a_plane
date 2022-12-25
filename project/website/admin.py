from flask import Flask, Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import User

admins = Blueprint('admins', __name__)

@admins.route('/', methods=['GET','POST'])
@login_required
def admin_home():
    return render_template('admin_home.html', user= current_user)


@admins.route('/user', methods=['GET','POST'])
@login_required
def admin_user():
    users = User.query.all()
    return render_template('admin_user.html', user=current_user, users=users)

