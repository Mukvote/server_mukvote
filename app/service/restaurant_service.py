from flask import jsonify
from flask_restful import abort

import json
import time
from datetime import date, datetime, timedelta
from sqlalchemy import and_

from app import db
from app.models.restaurant_model import Restaurant

from ..serializer import restaurant_schema

def get_restaurant_by_place(place):
    data = Restaurant.query.filter_by(restaurant_place=place).all()
    # restaurant_schema.dump(data)

    ret = []
    for result in data:
        ret.append(restaurant_schema.dump(result))
    print(ret)

    return ret


def search_result(word):
    #tag = request.form[word]
    search = "%{}%".format(word)
    data =  Restaurant.query.filter(Restaurant.restaurant_name.like(search)).all()

    ret = []
    for result in data:
        ret.append(restaurant_schema.dump(result))
    print(ret)

    return ret
