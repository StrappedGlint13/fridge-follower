from application import db
from application.models import Base
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

#connection table
DishProduct = db.Table("DishProduct", db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
db.Column("dish_id", db.Integer, db.ForeignKey("dish.id"))
)

class Dish(Base):
	
    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float, nullable=False)

    dishproduct = db.relationship('Product', secondary=DishProduct, lazy = 'subquery', 
backref=db.backref('dishes', lazy= True))

    def __init__(self, name, price):
        self.name = name
        self.price = price 
 
  
