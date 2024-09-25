from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import appdirs
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    # data = Column(String(10))
    # etc = Column(String(20))

data_dir = appdirs.user_data_dir("MyApp", "MyCompany")
os.makedirs(data_dir, exist_ok=True)

db_path = os.path.join(data_dir, 'my_database.db')

engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.create_all(engine)

metadata = Base.metadata