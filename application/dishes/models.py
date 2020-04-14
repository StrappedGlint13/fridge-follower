from application import db
from application.models import Base
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from application.products.models import Product

#connection table
DishProduct = db.Table("DishProduct", db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
db.Column("dish_id", db.Integer, db.ForeignKey("dish.id"))
)

class Dish(Base):
	
    price = db.Column(db.Float, nullable=False)

    dishproduct = db.relationship('Product', secondary= DishProduct, lazy = 'subquery', 
backref= db.backref('dishes', lazy= True))

    def __init__(self, name, price):

        self.price = 0

    def choises_dish_form():     
        stmt = text("SELECT * FROM Product")
        res = db.engine.execute(stmt)
        return res
 
  
