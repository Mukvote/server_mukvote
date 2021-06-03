from flask import jsonify
from flask_restful import abort

import json
import time
from datetime import datetime, timedelta
from sqlalchemy import and_

from app import db
from app.models.poll_model import Poll
from app.models.category_model import Category
from app.models.restaurant_model import Restaurant

from ..serializer import poll_schema, category_schema, restaurant_schema

def get_poll_list(id):
    data = Poll.query.filter_by(poll_id=id).first()
    place = data.place
    categories = Category.query.filter((Category.category_id==id)).all()

    data_list = dict()
    restaurant_list = dict()
    
    #priority 높은거 순서대로 5개씩 카테고리별 장소 이름 리턴
    for i in range (len(categories)):
        restaurant_by_category = Restaurant.query.filter(and_(Restaurant.restaurant_place==place,
        Restaurant.restaurant_category==categories[i].category_name)).order_by(Restaurant.restaurant_priority.desc()).limit(5).all()

        ret = []
        for result in restaurant_by_category:
            ret.append(restaurant_schema.dump(result))
        print(ret)
        
        restaurant_list = {categories[i].category_name:ret}
        print(restaurant_list)
        data_list.update(restaurant_list)

    return data_list

def save_new_poll(data):
    try:
        new_poll = Poll(
            owner = data['owner'],
            created_at = datetime.utcnow(),
            status = "open",
            shared_url = "empty",
            place = data['place'],
        )
        db.session.add(new_poll)
        db.session.commit()
    except Exception as e:
        print(e)
        abort(500)
    return new_poll

def save_category(data, poll_id):
    for category in data:
        print(category)
        try:
            add_category = Category(
                category_id = poll_id,
                category_name = category,
            )
            db.session.add(add_category)
            db.session.commit()
        except Exception as e:
            print(e)
            abort(500)

def update_url(id):
    try:
        poll = Poll.query.filter_by(poll_id=id).first()
        poll.shared_url = 'post/' + str(id)
        db.session.commit()
    except Exception as e:
        print(e)
        abort(500)
    return poll.shared_url