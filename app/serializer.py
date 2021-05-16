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

users_schema = UserSchema(many=True)

class PollSchema(ModelSchema):
    class Meta:
        model = Poll

poll_schema = PollSchema()

class VoteSchema(ModelSchema):
    class Meta:
        model = Vote

vote_schema = VoteSchema(many=True)

class RestaurantSchema(ModelSchema):
    class Meta:
        model = Restaurant

restaurant_schema = RestaurantSchema(many=True)

class CategorySchema(ModelSchema):
    class Meta:
        model = Category

category_schema = CategorySchema(many=True)