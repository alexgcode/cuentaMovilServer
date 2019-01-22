from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine creation
engine = create_engine('mysql://user:pass@x.x.x.x/test_cuentaMovil', pool_pre_ping=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
