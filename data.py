from sqlalchemy import Column, String, Integer, Date, Float
from DBConnection import Base

class Expense(Base):
    __tablename__= 'expense'

    id = Column(Integer, primary_key=True)
    description = Column(String(100))
    amount = Column(Float)
    date = Column(Date)

    def __init__(self, pdescription, pamount, pdate):
        self.description = pdescription
        self.amount = pamount
        self.date = pdate
