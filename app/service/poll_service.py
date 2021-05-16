from flask import jsonify
from flask_restful import abort

import json
import time
from datetime import datetime, timedelta

from app import db
from app.models.poll_model import Poll
from app.models.category_model import Category

from ..serializer import poll_schema, category_schema


def get_poll(id):
    print(id)
    data = Poll.query.filter_by(poll_id=id).first()
    data = poll_schema.dump(data)
    return data

def get_category_list(id):
    categories = Poll.query.filter((Poll.poll_id==id))
    categories = category_schema.dump(categories)
    return categories

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