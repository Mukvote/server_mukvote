from app import db
from .user_model import User

class Poll(db.Model):
    __tablename__ = 'poll'
    poll_id = db.Column(db.Integer, unique=True, primary_key = True, autoincrement=True, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    created_at = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.VARCHAR(255), nullable=False)
    shared_url = db.Column(db.VARCHAR(255), nullable=False)
    place = db.Column(db.VARCHAR(255), nullable=False)

    def __repr__(self):
        return "<Poll(poll_id='{}', owner='{}',created_at='{}', status='{}', shared_url='{}',place='{}')>"\
            .format(self.poll_id, self.owner, self.created_at, self.status, self.shared_url, self.place)