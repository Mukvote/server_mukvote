from flask import request, jsonify
from flask_restful import Resource, abort
import json

from ..service.restaurant_service import get_restaurant_by_place, search_result

class GetAllRestaurantByPlace(Resource):
    def get(self, place):
        output = get_restaurant_by_place(place)
        print(output)
        return jsonify({'restaurant_data': output})



class GetSearchResult(Resource):
    def get(self, word):
        output = search_result(word)
        
        return jsonify({'search_result': output})