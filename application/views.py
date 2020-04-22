from flask import render_template
from application import app
from application.usage.models import Waste

@app.route("/")
def index():
    return render_template("index.html", total_data=Waste.total_data())
