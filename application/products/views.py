from application import app, db
from flask import redirect, render_template, request, url_for
from application.products.models import Product

@app.route("/products", methods=["GET"])
def products_list():
    return render_template("products/list.html", products = Product.query.all())

@app.route("/products/new/")
def products_form():
    return render_template("products/new.html")


@app.route("/products/", methods=["POST"])
def products_create():
    product = Product(request.form.get("name"), request.form.get("amount"), request.form.get("price"))

    db.session().add(product)
    db.session().commit()
  
    return redirect(url_for("products_list"))
