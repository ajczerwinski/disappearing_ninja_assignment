from flask import Flask, render_template, request, redirect, session, flash, send_from_directory, url_for
app = Flask(__name__)
app.secret_key="SecreKeyMePls"
@app.route('/', methods = ['GET'])
def index():
	return render_template("/index.html")
@app.route("/ninja")
def ninja():
	turtle = "four_turtles"
	turtle_name = "all four turtles"
	return render_template("ninja.html", turtle_name=turtle_name, turtle=turtle)
@app.route('/ninja/<turtle>', methods=['GET'])
def ninja_color(turtle):
	if turtle == "purple":
		turtle_name = "Donatello"
		return render_template("/ninja.html", turtle_name=turtle_name, turtle=turtle)
	elif turtle == "red":
		turtle_name = "Raphael"
		return render_template("/ninja.html", turtle_name=turtle_name, turtle=turtle)
	elif turtle == "orange":
		turtle_name = "Michelangelo"
		return render_template("/ninja.html", turtle_name=turtle_name, turtle=turtle)
	elif turtle == "blue":
		turtle_name = "Leonardo"
		return render_template("/ninja.html", turtle_name=turtle_name, turtle=turtle)
	else:
		turtle = "meganfox"
		turtle_name = "Megan Fox"
		return render_template("/ninja.html", turtle_name=turtle_name, turtle=turtle)
app.run(debug=True)