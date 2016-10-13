from app import app

import sys
import json
import requests
import random

apiKey = app.config["API_KEY"]

BASE_URL = 'http://api.reimaginebanking.com'
API_KEY_PARAM = '?key={}'.format(apiKey)

# ===== CREATE CUSTOMER =====

customerUrl = BASE_URL + '/customers' + API_KEY_PARAM

customerData = {
	'first_name' : 'Mark',
	'last_name' : 'Zuckerberg',
	'address' : {
		'street_number' : '95',
		'street_name' : 'Dunster St.',
		'city' : 'Cambridge',
		'state' : 'MA',
		'zip' : '02238'
	}
}

customerPostResponse = requests.post(
	customerUrl,
	data=json.dumps(customerData),
	headers={'content-type':'application/json'})

# get the response and find the ID to create accounts for
jsonResponse = json.loads(customerPostResponse.text)
customerObj = jsonResponse['objectCreated']
print('Customer Created: ' + customerObj['first_name'] + ' ' + customerObj['last_name'])

customerId = jsonResponse["objectCreated"]["_id"]

# ===== CREATE ACCOUNTS =====

accountNames = ['Quincy Checking', 'Kirkland Savings', 'Lowell Checking', 'Mather Savings', 'Adams Checking']
accountType = ['Checking', 'Savings', 'Checking', 'Savings', 'Checking']

accountsUrl = BASE_URL + '/customers/{}/accounts'.format(customerId) + API_KEY_PARAM

print("")

# create 5 accounts
for i in range(0, 5):
	accountData = {
		'type' : accountType[i],
		'nickname' : accountNames[i],
		'rewards' : 0,
		'balance' : random.randrange(100, 100000),
		'account_number' : '1234567890123456'
	}

	accountPostResponse = requests.post(
		accountsUrl,
		data=json.dumps(accountData),
		headers={'content-type':'application/json'})

	accountJsonResponse = json.loads(accountPostResponse.text)
	accountObj = accountJsonResponse['objectCreated']

	print('Account Created: ' + accountObj['nickname'])



