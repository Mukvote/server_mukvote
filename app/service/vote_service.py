from app.service.poll_service import update_url
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
from app.models.vote_model import Vote

from ..serializer import poll_schema, category_schema, restaurant_schema, vote_schema

def get_vote_result(id):

    data = []
    distinct_vote = dict()
    localdata_ = Vote.query.filter(Vote.poll_id==id).all()
    for each_localdata in localdata_:
        if each_localdata.restaurant_id in distinct_vote.keys():
            distinct_vote[each_localdata.restaurant_id] += 1
        else:
            distinct_vote[each_localdata.restaurant_id] = 1
    
    for distinct_restaurant_id in distinct_vote.keys():
        data.append(distinct_restaurant_id)

    print(data)



    vote_list = dict()
    participant_num = dict()

    ret = []
    name_ret_list = []
    all_data = 0
    #각 restaurant 별, unique 투표결과
    for i in range (len(data)):
        print(data[i])
        print(type(data[i]))
        #true인거와s
        true_data = Vote.query.filter(and_(Vote.poll_id==id,Vote.restaurant_id==data[i],Vote.restaurant_vote == 1)).count()
        #각 아이디별 전부 개수
        all_data = Vote.query.filter(and_(Vote.poll_id==id,Vote.restaurant_id==data[i])).count()

        result = true_data/all_data

        restaurant_name = Restaurant.query.filter(Restaurant.restaurant_id==data[i]).first()

        #restaurant 이름 + result + 참여 전체 인원
        name_ret_list.append((restaurant_schema.dump(restaurant_name),result))
        #print(restaurant_schema.dump(restaurant_name))

    name_ret_list = sorted(name_ret_list, key = lambda x : -x[1])
    
    for name, result in name_ret_list:
        print(result)
        vote_list = {"restaurant_name":name['restaurant_name'],"result":result,"number_of_participant":all_data}
        print(vote_list)
        ret.append(vote_list)
        
    print(ret)

    return ret

def save_new_vote(data, poll_id, user_id):
    try:
        jsonArray = data.get('data')
        print(jsonArray)
        for each_data in jsonArray:
            print(each_data.get('restaurant_id'))
            print(each_data.get('restaurant_vote'))
            new_vote = Vote(
                poll_id = poll_id,
                user_id = user_id,
                restaurant_id = each_data.get('restaurant_id'),
                restaurant_vote = each_data.get('restaurant_vote')
            )
            print(new_vote)
            update_priority = Restaurant.query.filter(Restaurant.restaurant_id==each_data.get('restaurant_id')).first()
            print(update_priority)
            # update priority 확인 필요!!
            # 72번째줄에 new_vote>> update_priority로 아마 바꿔야 할것 같음.
            update_priority.restaurant_priority += 1
            db.session.add(new_vote)
            db.session.add(update_priority)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        abort(500)
    return 1


def is_vote(poll_id, user_id):
    print("is vote")
    print(poll_id)
    print(user_id)
    try:
        is_vote = Vote.query.filter(and_(Vote.poll_id==poll_id,Vote.user_id==user_id)).count()
        
    except Exception as e:
        print(e)
        db.session.rollback()
        abort(500)
    return is_vote