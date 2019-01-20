from data import Expense
from DBConnection import Session
from LogTest import logger

session = Session()

allExpenses = session.query(Expense).all() # expense is the class

print('\n### all expenses: ')
for expense in allExpenses:
    print(f'{expense.description} : {expense.amount} on date: {expense.date}')  # formater string evaluated each time runs
print('')


over30Expenses = session.query(Expense).filter(Expense.amount > 30)

print('\n### expenses over 30 soles: ')
for expense in over30Expenses:
    print(f'{expense.description} : {expense.amount} on date: {expense.date}')  # formater string evaluated each time runs
    logger.info(str('consulta condicionada exitosa ') + f'{expense.description} : {expense.amount} on \
     date: {expense.date}')
print('')

