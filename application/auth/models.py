from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"
  
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)

    product_id = db.relationship("Product", backref='account', cascade="all, delete", lazy=True)
    waste_id = db.relationship("Waste", backref='account', cascade="all, delete", lazy=True)
    dish_id = db.relationship("Dish", backref='account', cascade="all, delete", lazy=True)


    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]

	

