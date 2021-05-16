from flask import jsonify
from flask_restful import abort
from sqlalchemy import and_

from app import db
from app.models.user_model import User

from ..serializer import UserSchema

def save_new_user(data):
    # try:
        print('hello')
        new_user = User(
            user_name=data['user_name'],
            login_token=data['login_token']
        )
        print('hi')
        print(data['user_name'])
        print(data['login_token'])
        db.session.add(new_user)
        db.session.commit()
    # except Exception as e:
    #         print(e)
    #         abort(500)
        return new_user

def get_logininfo(data):
    check_user = User.query.filter(
            and_(user_name=data['user_name'], login_token=data['login_token'])).first()
    right_user = UserSchema().dump(check_user)
    if check_user:
        return "success"
    else:
        return "fail"