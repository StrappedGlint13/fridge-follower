from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class ProductForm(FlaskForm):
    name = StringField("Product name")
    amount = FloatField("Amount")
    price = FloatField("Price")
 
    class Meta:
        csrf = False
