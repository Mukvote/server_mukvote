from flask import request, jsonify
from flask_restful import Resource, abort
import json

from ..service.vote_service import save_new_vote, get_vote_result


class GetVoteResult(Resource):
    def get(self, poll_id):
        output = get_vote_result(poll_id)
        return jsonify({'poll_data': output})

class AddVote(Resource):
    def post(self, poll_id, user_id):
        data = request.get_json()
        vote = save_new_vote(data, poll_id, user_id)

        return jsonify({'result':vote})