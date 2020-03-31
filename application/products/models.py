from application import db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text

class Product(Base):

    name = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount 
        self.price = price 
 
    @staticmethod
    def find_users_products():
        stmt = text("SELECT Product.name, Product.amount, Product.price FROM Product"
                    " JOIN Account ON Product.account_id = Account.id"
                    " WHERE Product.account_id = :account_id"
		    " ORDER BY Product.price ASC").params(account_id=current_user.id)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"name":row[0], "amount":row[1], "price":row[2]})

        return response
