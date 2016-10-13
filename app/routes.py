from flask import render_template, request, redirect
from app import app
from app.utils import format_price
from enum import Enum

import requests
import json
import datetime

# get the API Key from the config file
apiKey = app.config["API_KEY"]

# enum for the medium of transfer
#  * balance - currency
#  * rewards - rewards points
class Medium(Enum):
	BALANCE = "balance"
	REWARDS = "rewards"

# http://www.davidadamojr.com/handling-cors-requests-in-flask-restful-apis/
@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
	return response



# ========== UPDATE BELOW THIS LINE ========== #



# This route loads the home screen.  Get all data necessary and pass it to the view. 
@app.route('/')
@app.route('/index')
def index():
	return render_template("home.html", accounts=[], transfers=[], format_price=format_price)

# This route should get the fields from the form and create a transfer POST request
@app.route('/transfer', methods=['POST'])
def postTransfer():
	return redirect("/index", code=302)




