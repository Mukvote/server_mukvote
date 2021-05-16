from app import db

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    login_token = db.Column(db.VARCHAR(200), unique=True, nullable=False)
    user_name = db.Column(db.VARCHAR(45), unique=True)

    def __repr__(self):
        return "<User(user_name='{}', user_id='{}', login_token='{}')>"\
            .format(self.user_name, self.user_id, self.login_token)