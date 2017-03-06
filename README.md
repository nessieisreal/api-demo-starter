# API Demo App for Harvard HCS Bootcamp

A simple banking dashboard showing a user's accounts and transfers.  It also allows user's to create new transfers.  This app demonstrates basic usage of APIs in a Python Flask application.  Makes use of the Nessie API for all data.

## Requirements  
* Python 2.7
* Pip for the appropriate version of Python (https://pip.pypa.io/en/stable/installing/)

## Installation

1. Clone the project.

	```
	git clone https://github.kdc.capitalone.com/tld509/api-demo-app.git
	```  

2. Navigate to the root of the project and create a file `config.py`.

3. Open the file you just created (config.py) and add your Nessie API key as a variable.  
	
	```
	API_KEY = "my_api_key"
	```  

4. Install required packages.

	```
	pip install -r requirements.txt
	```  

## Running the Application

Navigate to the root of the project and run:

	```
	python run.py
	```  

Navigate to **localhost:5000** to view the dashboard.

![Starter App](/app/img/starter.jpg)  
  

Once completed, the application should look like this:

![Finished Home Screen](/app/img/home-screen.jpg)

![Finished Transfer List](/app/img/transfer-list.jpg)
