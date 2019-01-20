from datetime import date
from data import Expense
from DBConnection import Session, engine, Base


Base.metadata.create_all(engine)

session = Session()

expenseDay2 = Expense("gasto2 SQLALCHEMY", 10, date(2019,1,20))

session.add(expenseDay2)
session.commit()
session.close()
