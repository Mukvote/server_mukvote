from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS

from .config import BaseConfig

db = SQLAlchemy()
migrate = Migrate(compare_type=True)

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(BaseConfig)
    api = Api(app)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    
    from .controller.user_controller import UserLogin, UserRegister
    api.add_resource(UserRegister, '/user_register')
    api.add_resource(UserLogin, '/user_login')

    from .controller.poll_controller import GetPoll, AddPoll, DeletePoll
    api.add_resource(GetPoll, '/poll/<poll_id>')
    api.add_resource(AddPoll, '/poll')
    api.add_resource(DeletePoll,'/poll/<poll_id>/<user_id>')


    from .controller.vote_controller import AddVote, GetVoteResult, IsVote
    api.add_resource(AddVote, '/vote/<poll_id>/<user_id>')  
    api.add_resource(GetVoteResult, '/vote/result/<poll_id>')
    api.add_resource(IsVote,'/check/<poll_id>/<user_id>')

    from .controller.restaurant_controller import GetAllRestaurantByPlace, GetSearchResult
    api.add_resource(GetAllRestaurantByPlace, '/restaurant/<place>')
    api.add_resource(GetSearchResult, '/restaurant/search/<word>')

    return app