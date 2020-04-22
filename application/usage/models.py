from application import db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text

class Waste(Base):

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
    def find_personal_waste():
        stmt = text("SELECT Waste.id, Waste.name, Waste.amount, Waste.price, Waste.date_created FROM Waste"
                    " JOIN Account ON Waste.account_id = Account.id"
                    " WHERE Waste.account_id = :account_id"
		    " ORDER BY Waste.date_created DESC").params(account_id=current_user.id)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "amount":row[2], "price":row[3], "date_created":row[4]})

        return response

    @staticmethod
    def total_data():
        stmt = text("SELECT Account.username,  SUM(Waste.amount) as wfood, SUM(Waste.price) as wprice, (SUM(Dish.amount) / (SUM(Waste.amount) + SUM(Dish.amount))) as usage FROM Waste"
         	        " LEFT JOIN Account ON Waste.account_id = Account.id"
                    " LEFT JOIN Product ON Product.account_id = Account.id"
                    " LEFT JOIN Dish ON Dish.account_id = Account.id"
		            " GROUP BY Account.id"
                    " ORDER BY Account.username ASC")

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"username": row[0], "wfood": row[1], "wprice": row[2], "usage": row[3]})

        return response

class Dish(Base):
	
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
    def find_personal_dishes():
        stmt = text("SELECT Dish.id, Dish.name, Dish.amount, Dish.price, Dish.date_created FROM Dish"
                    " JOIN Account ON Dish.account_id = Account.id"
                    " WHERE Dish.account_id = :account_id"
		    " ORDER BY Dish.date_created ASC").params(account_id=current_user.id)

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "amount":row[2], "price":row[3], "date_created":row[4]})

        return response
 


