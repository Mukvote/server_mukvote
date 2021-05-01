from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

from .config import BaseConfig

db = SQLAlchemy()
migrate = Migrate(compare_type=True)

def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    api = Api(app)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    from .controller.user_controller import UserList, UserPhone, UserAuth
    api.add_resource(UserList, '/user')
    api.add_resource(UserAuth, '/user/<email>')
    api.add_resource(UserPhone, '/user/phone')

    return app