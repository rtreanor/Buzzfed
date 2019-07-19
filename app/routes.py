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
    
@app.route('/dry_results', methods=['GET', 'POST'])
def results_drywall():
    userdata = formopener.dict_from(request.form)
    answer1 = userdata['answer1']
    answer2 = userdata['answer2']
    answer3 = userdata['answer3']
    answer4 = userdata['answer4']
    answer5 = userdata['answer5']
    answer6 = userdata['answer6']
    dry_total = model.calculate_dry_results(answer1, answer2, answer3, answer4, answer5, answer6)
    return render_template('dry_results.html', dry_total = dry_total)

@app.route('/birthday')
def birthday():
    return render_template('birthday.html')

@app.route('/birthday_results', methods=['GET', 'POST'])
def results_birth():
    userdata = formopener.dict_from(request.form)
    firstname = userdata['firstname'].decode('utf-8')
    lastname = userdata['lastname'].decode('utf-8')
    enterbd = userdata['enterbd'].decode('utf-8')
    return render_template('birthday_results.html', firstname = firstname, lastname = lastname, enterbd = enterbd)