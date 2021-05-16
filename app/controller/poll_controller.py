from flask import request, jsonify
from flask_restful import Resource, abort

from ..service.poll_service import get_poll, save_new_poll

class Poll(Resource):
    def get(self, poll_id):
        output = get_poll(poll_id)
        return jsonify({'poll_data': output})

class AddPoll(Resource):
    def post(self):
        data = request.get_json()
        poll_id = save_new_poll(data).poll_id

        # data['poll_id'] = poll_id
        return jsonify({'poll_id': poll_id})

