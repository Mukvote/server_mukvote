from app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    restaurant_id =  db.Column(db.Integer, primary_key=True, autoincrement = True)
    restaurant_name = db.Column(db.VARCHAR(255), nullable=False)
    restaurant_place = db.Column(db.VARCHAR(255), nullable=False)
    restaurant_category = db.Column(db.VARCHAR(255), nullable=False)
    restaurant_priority = db.Column(db.Integer, nullable=False)
    order_count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Restaurant(restaurant_id='{}', restaurant_name='{}',restaurant_place='{}', restaurant_category='{}', restaurant_priority='{}',order_count='{}')>"\
            .format(self.restaurant_id, self.restaurant_name, self.restaurant_place, self.restaurant_category, self.restaurant_priority, self.order_count)