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

    @staticmethod
    def find_personal_waste():
        stmt = text("SELECT * FROM Waste"
                    " JOIN Account ON Waste.account_id = Account.id"
                    " WHERE Waste.account_id = :account_id"
		    " ORDER BY Waste.date_created ASC").params(account_id=current_user.id)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id": row[0], "name":row[3], "amount":row[4], "price":row[5]})

        return response

    @staticmethod
    def total_amount_wfood():
        stmt = text("SELECT Account.username, SUM(Waste.amount) as wfood, SUM(Waste.price) as wprice FROM Waste"
         	        " LEFT JOIN Account ON Waste.account_id = Account.id"
		            " GROUP BY Account.id"
                    " ORDER BY Account.username ASC")

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"username": row[0], "wfood": row[1], "wprice": row[2]})

        return response

class Dish(Base):
	
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
    def find_personal_dishes():
        stmt = text("SELECT * FROM Dish"
                    " JOIN Account ON Dish.account_id = Account.id"
                    " WHERE Dish.account_id = :account_id"
		    " ORDER BY Dish.date_created ASC").params(account_id=current_user.id)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id": row[0], "name":row[3], "amount":row[4], "price":row[5]})

        return response
 


