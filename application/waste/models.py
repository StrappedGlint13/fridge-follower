from application import db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text

class Waste(Base):

    name = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount 
        self.price = price 
 
