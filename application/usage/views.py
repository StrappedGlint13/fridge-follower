from flask_login import login_required, current_user
from flask import redirect, render_template, request, url_for, flash

from application import app, db
from application.usage.models import Waste, Dish, favorites

@app.route("/usage", methods=["GET"])
@login_required
def usage_list():
	return render_template("usage/list.html", waste=Waste.find_personal_waste(), dishes=Dish.find_personal_dishes())

@app.route("/usage/deletewaste/<waste_id>/", methods=["GET", "POST"])
@login_required
def delete_permanently(waste_id):
	waste = Waste.query.get(waste_id)

	if not waste.account_id == current_user.id:
		 return redirect(url_for("usage_list"))
	
	db.session().delete(waste)
	db.session().commit()
  
	return redirect(url_for("usage_list"))

@app.route("/usage/deletedish/<dish_id>/", methods=["GET", "POST"])
@login_required
def delete_dish_permanently(dish_id):
	dish = Dish.query.get(dish_id)

	if not dish.account_id == current_user.id:
		 return redirect(url_for("usage_list"))
	
	db.session().delete(dish)
	db.session().commit()
  
	return redirect(url_for("usage_list"))

@app.route("/usage/addfavorite/<dish_id>/", methods=["POST","GET"])
@login_required
def add_favorite(dish_id):

	dish = Dish.query.get(dish_id)

	if  Dish.find_id(dish_id):
		 flash("This item is already added to favorites")
		 return (redirect(url_for("usage_list")))

	stmt = favorites.insert().values(dish_id=dish_id, account_id=current_user.id)
	db.session().execute(stmt)
	db.session().commit()
	return redirect(url_for("usage_list"))

@app.route("/usage/showfavorites/", methods=["GET"])
@login_required
def show_favorites():
	return render_template("usage/favorites.html", favorites=Dish.find_favorites())

	return redirect(url_for("usage_list"))

