from app import app

import sys
import json
import requests
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--delete', help='delete existing data prior to creating new data', action='store_true')
args = parser.parse_args()

apiKey = app.config["API_KEY"]

BASE_URL = 'http://api.reimaginebanking.com'
API_KEY_PARAM = '?key={}'.format(apiKey)

# ===== REFRESH DATA =====

if args.delete:
	print "\nDeleting:"
	print "========="
	
	objectsToDelete = ['Customers', 'Accounts']

	for i in range (0, len(objectsToDelete)):
		deleteUrl = BASE_URL + '/data' + API_KEY_PARAM + '&type={}'.format(objectsToDelete[i])
		deleteResponse = requests.delete(deleteUrl)
		if deleteResponse.status_code != 204:
			print "!! Error removing {}".format(objectsToDelete[i])	+ " !!"
		else:
			print "Removed all {}".format(objectsToDelete[i])

# ===== CREATE CUSTOMER =====

print "\nCreating:"
print "========="

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

name = customerObj['first_name'] + ' ' + customerObj['last_name']

if customerPostResponse.status_code != 201:
	print "!! Error creating {}".format(name)	+ " !!"
	print "Cannot create accounts without customer.  Terminating..."
	print"\n"
	sys.exit()
else:
	print('Customer Created: ' + name)

customerId = jsonResponse["objectCreated"]["_id"]

# ===== CREATE ACCOUNTS =====

accountNames = ['Quincy Checking', 'Kirkland Savings', 'Lowell Checking', 'Mather Savings', 'Adams Checking']
accountType = ['Checking', 'Savings', 'Checking', 'Savings', 'Checking']

accountsUrl = BASE_URL + '/customers/{}/accounts'.format(customerId) + API_KEY_PARAM

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

	if accountPostResponse.status_code != 201:
		print "!! Error creating {}".format(accountObj['nickname'])	+ " !!"
	else:
		print('Account Created: ' + accountObj['nickname'])



