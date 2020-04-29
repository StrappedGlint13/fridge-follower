from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("MyFridge")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("MyFridge", [validators.Length(min=2)])
    password = PasswordField("Password", [validators.Length(min=8, max=30, message="the password must be between 8-30 characters")])
    email = StringField("Email", [validators.Length(min=2)])

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    newusername = StringField("MyFridge", [validators.Length(min=2)])
    newemail = StringField("Email", [validators.Length(min=2)])

    class Meta:
        csrf = False

class ChangePassForm(FlaskForm):
    oldpass = PasswordField("Old password", [validators.Length(min=2)])
    newpass = PasswordField("New password", [validators.Length(min=2, max=30, message="the password must be between 8-30 characters")])
    confirmpass = PasswordField("Confrim new password", [validators.Length(min=2, max=30)])

    class Meta:
        csrf = False



