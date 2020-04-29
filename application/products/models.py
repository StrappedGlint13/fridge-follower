from application import db
from application.models import Base
from application.auth.models import User
from flask_login import current_user
from sqlalchemy.sql import text


class Product(Base):

    name = db.Column(db.String(144), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete='CASCADE'),
                           nullable=False)

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount 
        self.price = price 
 
    @staticmethod
    def find_users_products():
        stmt = text("SELECT * FROM Product"
                    " JOIN Account ON Product.account_id = Account.id"
                    " WHERE Product.account_id = :account_id"
		    " ORDER BY Product.name ASC").params(account_id=current_user.id)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id": row[0], "name":row[3], "amount":row[4], "price":row[5]})

        return response

    @staticmethod
    def count_products():
        stmt = text("SELECT Product.name, COUNT(*) as total_products FROM Product"
                    " JOIN Account ON Product.account_id = Account.id"
                    " WHERE Product.account_id = :account_id"
                    " GROUP BY Account.id"
            " ORDER BY Product.name ASC").params(account_id=current_user.id)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id": row[0], "total_products": row[1]})

        return response