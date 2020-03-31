from flask_login import login_required, current_user
from flask import redirect, render_template, request, url_for

from application import app, db
from application.products.models import Product
from application.products.forms import ProductForm

@app.route("/products", methods=["GET"])
@login_required
def products_list():
    return render_template("products/list.html", products=Product.find_users_products())

@app.route("/products/new/")
@login_required
def products_form():
    return render_template("products/new.html", form = ProductForm())

@app.route("/products/<product_id>", methods=["POST","GET"])
@login_required
def change_amount(product_id):

    t = Product.query.get(product_id)
    t.amount = request.form.get("amount")  
    db.session().commit()
  
    return redirect(url_for("products_list"))


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

@app.route("/products/<product_id>/", methods=["POST"])
@login_required
def products_delete(product_id): 
    product = Product.query.get(product_id)
	

    db.session().delete(product)
    db.session().commit()
  
    return redirect(url_for("products_list"))
