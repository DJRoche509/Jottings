from flask import Flask, redirect, url_for, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')


app.config.from_object('config')  # Load configuration from config.py
'''app.config['SECRET_KEY'] = config.SECRET_KEY'''

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

# Import routes after initializing the app object
from app.routes import *