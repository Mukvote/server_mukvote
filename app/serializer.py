# from datetime import datetime
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from .models.user_model import User
from .models.poll_model import Poll
from .models.vote_model import Vote
from .models.restaurant_model import Restaurant
from .models.category_model import Category

class UserSchema(ModelSchema):
    class Meta:
        model = User

users_schema = UserSchema()

class PollSchema(ModelSchema):
    class Meta:
        model = Poll

poll_schema = PollSchema()

class VoteSchema(ModelSchema):
    class Meta:
        model = Vote

vote_schema = VoteSchema()

class RestaurantSchema(ModelSchema):
    class Meta:
        model = Restaurant

restaurant_schema = RestaurantSchema()

class CategorySchema(ModelSchema):
    class Meta:
        model = Category

category_schema = CategorySchema()