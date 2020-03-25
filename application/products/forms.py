from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators

class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=2)])
    amount = FloatField("Amount", [validators.NumberRange(min=0, message="The amount of product can't be negative. Type the amount x.xx with numbers")])
    price = FloatField("Price",  [validators.NumberRange(min=0, message="The price can't be negative. Type the price x.xx with numbers")])
 
    class Meta:
        csrf = False
