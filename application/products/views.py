from flask_login import login_required, current_user
from flask import redirect, render_template, request, url_for, flash

from application import app, db
from application.products.models import Product
from application.products.forms import ProductForm
from application.usage.models import Waste, Dish

@app.route("/products", methods=["GET"])
@login_required
def products_list():
    return render_template("products/list.html", products=Product.find_users_products(), items=Product.count_products())

@app.route("/products/new/")
@login_required
def products_form():
    return render_template("products/new.html", form = ProductForm())


@app.route("/products/", methods=["POST"])
@login_required
def products_create(): 
    form = ProductForm(request.form)
	
    if not form.validate():
        return render_template("products/new.html", form = form)

    product = Product(request.form.get("name"), request.form.get("amount"), request.form.get("price"))

    product.account_id = current_user.id

    db.session().add(product)
    db.session().commit()
  
    return redirect(url_for("products_list"))

@app.route("/product/delete/<product_id>/", methods=["GET", "POST"])
@login_required
def products_delete(product_id):
    product = Product.query.get(product_id)

    if not product.account_id == current_user.id:
         return redirect(url_for("products_list"))
	
    db.session().delete(product)
    db.session().commit()
  
    return redirect(url_for("products_list"))


@app.route("/products/throwaway/<product_id>", methods=["POST","GET"])
@login_required
def throw_waste(product_id):

    t = Product.query.get(product_id)

    if (is_number(request.form.get("waste")) == True):

        throw = float(request.form.get("waste"))

        if throw > t.amount or throw < 0:
            flash('Enter a valid numeric value for wasted food')
            return redirect(url_for("products_list"))

        lost_money = (throw/t.amount)*t.price
        t.price = t.price - lost_money

        t.amount = t.amount - float(request.form.get("waste")) 

        if (t.amount == 0):
            products_delete(product_id)

        waste = Waste(t.name, request.form.get("waste"), lost_money) 

        waste.account_id = current_user.id	

        db.session().add(waste)
        db.session().commit()
      
        return redirect(url_for("products_list"))

    flash('Enter a valid numeric value for wasted food')
    return redirect(url_for("products_list"))

@app.route("/products/eatsimple/<product_id>", methods=["POST","GET"])
@login_required
def eat_simple(product_id):

    t = Product.query.get(product_id)

    if (is_number(request.form.get("amount")) == True):

        eat = float(request.form.get("amount"))
    
        if eat > t.amount or eat < 0:
         flash('Enter a valid numeric value for used food')
         return redirect(url_for("products_list"))

        cost = (eat/t.amount)*t.price
        t.price = t.price - cost
        t.amount = t.amount - float(request.form.get("amount")) 

        if (t.amount == 0):
         products_delete(product_id)

        dish = Dish(t.name, request.form.get("amount"), cost) 

        dish.account_id = current_user.id  

        db.session().add(dish)
        db.session().commit()
  
        return redirect(url_for("products_list"))

    flash('Enter a valid numeric value for used food')
    return redirect(url_for("products_list"))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


