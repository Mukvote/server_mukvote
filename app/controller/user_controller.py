from flask import request, jsonify
from flask_restful import Resource, abort

from ..service.user_service import save_new_user,get_logininfo

class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        print('hi')
        save_new_user(data)

        return jsonify({'result': "success"})

class UserLogin(Resource):
    def get(self):
        data = request.get_json()
        output = get_logininfo(data)
        return jsonify({'result':output})