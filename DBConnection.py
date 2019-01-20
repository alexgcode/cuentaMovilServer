from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine creation
engine = create_engine('mysql://alex2:ubuntu@18.212.169.220:3306/test_cuentaMovil', pool_pre_ping=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
