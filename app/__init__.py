from flask import Flask

app = Flask(__name__)
app.config.from_object('config')  # load config file into the app
from app import routes