from datetime import date
from data import expense
from DBConnection import Session, engine, Base


Base.metadata.create_all(engine)

session = Session()

expenseDay1 = expense("pruebaSQLALCHEMY", 34, date(2019,1,19))

session.add(expenseDay1)
session.commit()
session.close()
