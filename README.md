# API Demo App for Harvard HCS Bootcamp

A simple banking dashboard showing a user's accounts and transfers.  It also allows user's to create new transfers.  This app demonstrates basic usage of APIs in a Python Flask application.  Makes use of the Nessie API for all data.

## Requirements  
* Python 2.7
* Pip for the appropriate version of Python (https://pip.pypa.io/en/stable/installing/)

## Installation  

1. `git clone https://github.kdc.capitalone.com/tld509/api-demo-app.git`
2. `cd api-demo-app`
3. `touch config.py`
4. Open the file you just created (config.py) and add your Nessie API key as a variable.  
    `API_KEY = "my_api_key"`  
5. `pip install requirements.txt`
6. `python run.py`
7. Navigate to **localhost:5000** to view the dashboard.


![Alt text](/app/img/home-screen.jpg)

![Alt text](/app/img/transfer-list.jpg)
