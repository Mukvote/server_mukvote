from flask import jsonify
from flask_restful import abort

from datetime import datetime, timedelta

from app import db
from app.models.user_model import User

from ..serializer import UserSchema

def get_all_users():
    all_users = User.query.all()
    all_users = UserSchema().dump(all_users)
    return all_users

def is_new_user(email):
    user = User.query.filter_by(email=email).first()
    if not user: # Yes It's New User
        return True
    else:
        update_user_log(email)
        return False

def update_user_log(email):
    try:
        user = User.query.filter_by(email=email).first()
        user.cnt_login += 1
        user.last_login = datetime.utcnow() + timedelta(hours=9)
        db.session.commit()
    except Exception as e:
        print(e)
        abort(500)
    return user

def save_new_user(data):
    try:
        new_user = User(
            name=data['name'],
            email=data['email'],
            photo_url=data['photo_url'],
            uid=data['uid'],
            registered_on=datetime.utcnow() + timedelta(hours=9),
            last_login=datetime.utcnow() + timedelta(hours=9),
            cnt_login=0
        )
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
            print(e)
            abort(500)
    return new_user

def edit_user_phonenumber(data):
    try:
        user = User.query.filter_by(email=data['email']).first()
        user.phone = data['phone']
        db.session.commit()
    except Exception as e:
            print(e)
            abort(500)