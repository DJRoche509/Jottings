from flask import render_template

# Import the Flask app instance from app package
from app import app  


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/addNote')
def addNote():
    return render_template('addNote.html')