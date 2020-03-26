from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Your name", [validators.Length(min=2)])
    username = StringField("Fridge name", [validators.Length(min=2)])
    password = PasswordField("Password", [validators.Length(min=8, max=30, message="the password must be between 8-30 characters")])
    email = StringField("Email", [validators.Length(min=2)])

    class Meta:
        csrf = False
