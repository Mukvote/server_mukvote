import bcrypt

from flask import jsonify
from flask_restful import abort
from sqlalchemy import and_

from app import db
from app.models.user_model import User

from ..serializer import users_schema

def save_new_user(data):
    check_user = User.query.filter_by(user_name=data['user_name']).first()
    if check_user:
        return -1

    try:
        bytes_password = str.encode(data['login_token'])
        bytes_hashed_password = bcrypt.hashpw(password=bytes_password, salt=bcrypt.gensalt())
        print(bytes_hashed_password)
        new_user = User(
            user_name=data['user_name'],
            login_token=bytes_hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
            print(e)
            db.session.rollback()
            abort(500)
    return 1

def get_logininfo(data):
    check_user = User.query.filter_by(user_name=data['user_name']).first()
    if check_user:
        bytes_password = str.encode(data['login_token']) #// sentone check
        bytes_db_pw = check_user.login_token.encode('utf-8')
        print(bytes_db_pw)
        print(bytes_password)
        is_same = bcrypt.checkpw(bytes_password, bytes_db_pw)

        if is_same:
            return check_user.user_id
        else:
            return -1
    else:
        return -1