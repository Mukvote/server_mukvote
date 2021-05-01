from flask import request, jsonify
from flask_restful import Resource, abort

from ..service.user_service import get_all_users, save_new_user, edit_user_phonenumber, is_new_user

class UserList(Resource):
    def get(self):
        output = get_all_users()
        return jsonify({'data': output})

    def post(self):
        data = request.get_json()
        save_new_user(data)

        return jsonify({'result': "Success"})

class UserAuth(Resource):
    def get(self, email):
        return jsonify({'is_new': is_new_user(email)})
    
class UserPhone(Resource):
    def put(self):
        data = request.get_json()
        edit_user_phonenumber(data)

        return jsonify({'result': "Success"})

    