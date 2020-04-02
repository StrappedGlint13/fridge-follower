from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators

class HistoryForm(FlaskForm):
    
 
    class Meta:
        csrf = False
