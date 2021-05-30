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

    from .controller.poll_controller import GetPoll, AddPoll
    api.add_resource(GetPoll, '/poll/<poll_id>')
    api.add_resource(AddPoll, '/poll')


    return app