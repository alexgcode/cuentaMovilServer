from flask import Flask, jsonify
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundoss'


@app.route('/expenses')
def expenses():
    return 'TODO'


@app.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense(expense_id):
    return 'TODO'

#app.run()