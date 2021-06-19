from flask import request, jsonify
from flask_restful import Resource, abort
import json

from ..service.vote_service import save_new_vote, get_vote_result, is_vote


class GetVoteResult(Resource):
    def get(self, poll_id):
        output = get_vote_result(poll_id)
        print(output)
        return jsonify({'poll_data': output})

class AddVote(Resource):
    def post(self, poll_id, user_id):
        data = request.get_json()
        print(data)
        vote = save_new_vote(data, poll_id, user_id)

        return jsonify({'result':vote})

class IsVote(Resource):
    def get(self, poll_id, user_id):
        print(poll_id)
        print(user_id)
        vote = is_vote(poll_id, user_id)
        print(vote)

        return jsonify({'check_result':vote})
        