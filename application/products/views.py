from application import app, db
from flask import redirect, render_template, request, url_for
from application.products.models import Product

@app.route("/products", methods=["GET"])
def products_index():
    return render_template("products/list.html", products = Product.query.all())

@app.route("/products/new/")
def products_form():
    return render_template("products/new.html")

@app.route("/products/", methods=["POST"])
def products_create():
    t = Product(request.form.get("name", "amount", "price"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("products_index"))
