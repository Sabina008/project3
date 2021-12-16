"""A simple flask web app"""
import re
import pandas as pd
from flask import Flask, request
from flask import render_template
from calc.calculator import Calculator
app = Flask(__name__)

@app.route("/")
def index():
    """index  Route Response"""
    return render_template('index.html')

@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    if request.method == 'POST':
        #get the values out of the form
        validate_value1 = re.match(r'^\-?\d*[\w.@]?\d*$', request.form['value1'])
        validate_value2 = re.match(r'^\-?\d*[\w.@]?\d*$', request.form['value2'])
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'Invalid Input: A value for operation cannot be empty.'
            return render_template('basicform.html', error=error)
        elif validate_value1 is None or validate_value2 is None:
            error = 'Invalid Input: Values can only be numbers'
            return render_template('basicform.html', error=error)
        # elif validate_value2 is None:
        #     error = 'Invalid Input: Values can only be numbers'
        #     return render_template('basicform.html', error=error)

    else:
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        #make the tuple
        my_tuple = (value1, value2)
        #this will call the correct operation
        getattr(Calculator, operation)(my_tuple)
        result = str(Calculator.get_last_result_value())
        data = {
            'OPERATION': [operation],
            'VALUE_A': [value1],
            'VALUE_B': [value2],
            'RESULT': [result]
        }

        #write to CSV - pass value 1 and 2 to csv
        operations = pd.DataFrame(data)
        operations.to_csv('operationsdata.csv', mode='a', index=False, header=False)
        #convert CSV to html
        data = pd.read_csv('operationsdata.csv', header=0)
        mydata = data.values

        return render_template('result.html',value1=value1, value2=value2, operation
        =operation, result=result)
    # Displays the form because if it isn't a post it is a get request
    else:
        return render_template('basicform.html')

@app.route("/browserwars1")
def browserwars1():
    """bad calc Route Response"""
    return render_template('browserwars1.html')

@app.route("/browserwars2")
def browserwars2():
    """bad calc Route Response"""
    return render_template('browserwars2.html')

@app.route("/history")
def history():
    """bad calc Route Response"""
    return render_template('history.html')

@app.route("/branch1")
def branch1():
    """bad calc Route Response"""
    return render_template('branch1.html')

@app.route("/branch2")
def branch2():
    """bad calc Route Response"""
    return render_template('branch2.html')