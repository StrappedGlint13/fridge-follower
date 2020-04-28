from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
  
from application import app, db, bcrypt
from application.auth.models import User
from application.products.models import Product
from application.usage.models import Waste, Dish
from application.auth.forms import LoginForm
from application.auth.forms import RegisterForm
from application.auth.forms import EditForm
from application.auth.forms import ChangePassForm


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()

    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")

    if not bcrypt.check_password_hash(user.password, form.password.data):
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))  


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  

@app.route("/auth/create", methods=["GET", "POST"])
def account_create(): 
    form = RegisterForm(request.form)

    if not form.validate():   
        return render_template("auth/registerform.html", form = form)

    if User.query.filter_by(username=form.username.data).first():
        form.username.errors.append("Username is already in use")
        return render_template("auth/registerform.html", form = form)

    user = User(request.form.get("name"), request.form.get("username"), bcrypt.generate_password_hash(form.password.data).decode('utf-8'), request.form.get("email"))

    db.session().add(user)
    db.session().commit()
  
    return render_template("auth/loginform.html", form = LoginForm())

@app.route("/auth/edit/", methods = ["GET", "POST"])
@login_required
def user_edit():
    user = User.query.get(current_user.id)

    if request.method == "GET":
        form = EditForm()

        form.newname.data = user.name
        form.newusername.data = user.username
        form.newemail.data = user.email

        return render_template("auth/editform.html", form = form)

    form = EditForm(request.form)

    if not form.validate():
        return render_template("auth/editform.html", form = form)

    user.name = form.newname.data
    user.username = form.newusername.data
    user.email 	= form.newemail.data 
    
    db.session().commit()
     
    return redirect(url_for("index"))

@app.route("/auth/change/", methods = ["GET", "POST"])
@login_required
def change_password():

    user = User.query.get(current_user.id)

    if request.method == "GET":
        return render_template("auth/changepassform.html", form = ChangePassForm())

    form = ChangePassForm(request.form)
    
    if  bcrypt.check_password_hash(user.password, form.oldpass.data) and form.newpass.data == form.confirmpass.data:
        user.password = bcrypt.generate_password_hash(form.newpass.data).decode('utf-8')

        db.session().commit()
        return redirect(url_for("user_edit"))
    else:
        return render_template("auth/changepassform.html", form = form,
                                error = "Passwords did not match or the old password was wrong")

@app.route("/auth/delete/<account_id>", methods = ["POST", "GET"])
@login_required
def user_delete(account_id):

    user = User.query.get(account_id)

    db.session().delete(user)
    db.session().commit()
    
    return redirect(url_for("auth_logout"))



