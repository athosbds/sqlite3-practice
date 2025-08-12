from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


engine = create_engine('mysql+pymysql://root:root%40%2323@localhost/my_database')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

# CRUD
def create_user(name, age):
    new = User(name=name, age=age)
    session.add(new)
    session.commit()
def list_users():
    users = session.query(User).all()
    for user in users:
        print(f'ID: {user.id} - Nome: {user.name} - Idade: {user.age}')
def delete_user(user):
    user_delete = session.query(User).filter(user)
    session.delete(user_delete)
    session.commit()
# continuando....
    
