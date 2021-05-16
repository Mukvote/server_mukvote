from flask import jsonify
from flask_restful import abort

import time
from datetime import datetime, timedelta

from app import db
from app.models.poll_model import Poll
from app.models.category_model import Category

from ..serializer import poll_schema


def get_poll(id):
    print(id)
    data = Poll.query.filter_by(poll_id=id).first()
    data = poll_schema.dump(data)
    return data


def save_new_poll(data):
    try:
        new_poll = Poll(
            owner = data['owner'],
            created_at = datetime.utcnow(),
            status = "open",
            shared_url = "temp",
            place = data['place'],
        )
        db.session.add(new_poll)
        db.session.commit()
    except Exception as e:
        print(e)
        abort(500)
    return new_poll