from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
  
from application import app, db, bcrypt
from application.auth.models import User
from application.products.models import Product
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
    if not user or not bcrypt.check_password_hash(user.password, form.password.data):
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

    user = User(request.form.get("name"), request.form.get("username"), bcrypt.generate_password_hash(form.password.data), request.form.get("email"))


    db.session().add(user)
    db.session().commit()
  
    return redirect(url_for("index")) 

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
     
    flash("Details changed successfully", "info")
    return redirect(url_for("index"))

@app.route("/auth/change/", methods = ["GET", "POST"])
@login_required
def change_password():

    user = User.query.get(current_user.id)

    if request.method == "GET":
        return render_template("auth/changepassform.html", form = ChangePassForm())

    form = ChangePassForm(request.form)
    
    if  form.oldpass.data == user.password and form.newpass.data == form.confirmpass.data:
        user.password = form.newpass.data

        db.session().commit()
        return redirect(url_for("index"))
    else:
        return redirect(url_for("change_password", error = "Passwords did not match" ))

@app.route("/auth/delete/<account_id>", methods = ["POST"])
@login_required
def user_delete(account_id):
    
    Product.query.filter_by(account_id=account_id).delete()
    user = User.query.get(account_id)

    db.session().delete(user)
    db.session().commit()
    
    return redirect(url_for("auth_logout"))

