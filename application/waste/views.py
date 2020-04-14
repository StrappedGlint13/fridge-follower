from flask_login import login_required, current_user
from flask import redirect, render_template, request, url_for

from application import app, db
from application.waste.models import Waste

@app.route("/waste", methods=["GET"])
@login_required
def waste_list():
    return render_template("waste/list.html", waste=Waste.find_personal_waste())

@app.route("/waste/delete/<waste_id>/", methods=["GET", "POST"])
@login_required
def delete_permanently(waste_id):
    waste = Waste.query.get(waste_id)
	
    db.session().delete(waste)
    db.session().commit()
  
    return redirect(url_for("waste_list"))


