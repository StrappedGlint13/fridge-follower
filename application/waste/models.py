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
        stmt = text("SELECT Account.username, COUNT(Waste.amount) AS wfood FROM Waste"
         	        " LEFT JOIN Account ON Waste.account_id = Account.id"
		            " GROUP BY Account.id")

        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"username": row[0], "wfood": row[1]})

        return response
