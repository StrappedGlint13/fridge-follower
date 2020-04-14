from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class AddDishForm(FlaskForm):


    class Meta:
        csrf = False

