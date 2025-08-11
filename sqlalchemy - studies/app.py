from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import app
Base = declarative_base()

class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

engine = create_engine('mysql+pymysql://root:root%40%2323@localhost/my_database') #CREATE DATABASE meu_banco;
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session

