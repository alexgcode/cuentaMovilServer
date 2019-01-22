from flask import Flask, jsonify, request
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
    data = expense_schema.dump(expenses, many=True).data
    return jsonify({"expenses":data})


@app.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense(expense_id):
    expense = session.query(Expense).filter(Expense.id == expense_id)
    data = expense_schema.dump(expense, many=True).data  #why only works with many=True ?
    return jsonify({"expense": data})



@app.route('/addexpense', methods=['POST'])
def add_expense():
    expense = expense_schema.load(request.get_json(), session=session).data  # request.get_json()
    session.add(expense)
    session.commit()
    return "", 204



app.run()
