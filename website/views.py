from flask import *
from .models import predict

views = Blueprint("views" ,__name__)
irissp = ["Iris-Setosa", "Iris-Versicolour", "Iris-Virginica"]

@views.route("/", methods=["POST", "GET"])
def home():
	if request.method=="POST":
		sepal_length = request.form["sepal-length"]
		sepal_width = request.form["sepal-width"]
		petal_length = request.form["petal-length"]
		petal_width = request.form["petal-width"]
		data = [sepal_length, sepal_width, petal_length, petal_width]
		species = predict(data)
		
		return render_template("home.html", result=irissp[species[0]])
	return render_template('home.html', result=False)

@views.route("/about")
def about():
	return render_template("about.html")