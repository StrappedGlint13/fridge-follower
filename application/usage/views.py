from flask_login import login_required, current_user
from flask import redirect, render_template, request, url_for

from application import app, db
from application.usage.models import Waste, Dish

@app.route("/usage", methods=["GET"])
@login_required
def usage_list():
    return render_template("usage/list.html", waste=Waste.find_personal_waste(), dishes=Dish.find_personal_dishes())

@app.route("/usage/deletewaste/<waste_id>/", methods=["GET", "POST"])
@login_required
def delete_permanently(waste_id):
    waste = Waste.query.get(waste_id)
	
    db.session().delete(waste)
    db.session().commit()
  
    return redirect(url_for("usage_list"))

@app.route("/usage/deletedish/<dish_id>/", methods=["GET", "POST"])
@login_required
def delete_dish_permanently(dish_id):
    dish = Dish.query.get(dish_id)
	
    db.session().delete(dish)
    db.session().commit()
  
    return redirect(url_for("usage_list"))

