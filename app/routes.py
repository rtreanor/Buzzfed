from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/drywall')
def dry_wall():
    return render_template('drywall.html')
    
# @app.route('/results_drywall')