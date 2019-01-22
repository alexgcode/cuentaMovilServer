from flask import Flask, jsonify
from marshmallow_sqlalchemy import ModelSchema
from DBConnection import Session
from data import Expense

app = Flask(__name__)
session = Session()


class ExpenseSchema(ModelSchema):
    class Meta:
        model = Expense


expense_schema = ExpenseSchema(strict=True)


@app.route('/')
def index():
    return 'hola'


@app.route('/expenses')
def expenses():
    expenses = session.query(Expense)
    data = expense_schema.dump(expenses, many=True)
    return jsonify({"expenses":data})


@app.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense(expense_id):
    expense = session.query(Expense).filter(Expense.id == expense_id)
    data = expense_schema.dump(expense, many=True)  #why only works with many=True ?
    return jsonify({"expense": data})


app.run()
