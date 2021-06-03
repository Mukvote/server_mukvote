from flask import request, jsonify
from flask_restful import Resource, abort
import json

from ..service.poll_service import get_poll_list, save_new_poll, save_category, update_url

class GetPoll(Resource):
    def get(self, poll_id):
        output = get_poll_list(poll_id)
        return jsonify({'poll_data': output})

class AddPoll(Resource):
    def post(self):
        data = request.get_json()
        poll = save_new_poll(data)
        poll_id = poll.poll_id

        save_category(data['categories'], poll_id)
        url = update_url(poll_id)

        print(poll_id)
        print(url)

        return jsonify({'poll_id': poll_id, 'shared_url': url})

