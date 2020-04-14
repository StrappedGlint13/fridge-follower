from flask import render_template
from application import app
from application.waste.models import Waste

@app.route("/")
def index():
    return render_template("index.html", total_amount_wfood=Waste.total_amount_wfood())
