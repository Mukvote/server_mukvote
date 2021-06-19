from app import db
from .poll_model import Poll
from sqlalchemy.orm import backref

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, db.ForeignKey('poll.poll_id'), primary_key=True)
    category_name = db.Column(db.VARCHAR(255), primary_key=True, nullable=False)

    poll = db.relationship('Poll',backref=backref("children2", cascade="all,delete"))

    def __repr__(self):
        return "<Category(category_id='{}', category_name='{}')>"\
            .format(self.category_id, self.category_name)
