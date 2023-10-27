from flask import Flask
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config')  
'''app.config['SECRET_KEY'] = config.SECRET_KEY'''

# Import routes after initializing the app object
from app import routes