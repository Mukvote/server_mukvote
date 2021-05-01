from app import db
from .user_model import User
from .poll_model import Poll
from .restaurant_model import Restaurant

class Vote(db.Model):
    __tablename__ = 'vote'
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.poll_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.restaurant_id'), primary_key=True)
    restaurant_vote = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return "<Vote(poll_id='{}', user_id='{}',restaurant_id='{}', restaurant_vote='{}')>"\
            .format(self.poll_id, self.user_id, self.restaurant_id, self.restaurant_vote)
