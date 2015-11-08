from flask import Flask, render_template, request, redirect, session, flash, send_from_directory
import random
app = Flask(__name__)
app.secret_key="SecreKeyMePls"
@app.route('/')
def index():
	return render_template("index.html")
app.run(debug=True)