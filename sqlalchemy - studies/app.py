from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


engine = create_engine('mysql+pymysql://root:rootlanguageauth2008@localhost/inventory_db')
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
    user_delete = session.query(User).filter(User.id == user).first()
    if user_delete:
        session.delete(user_delete)
        session.commit()
    else:
        print(f'Não Encontrado: {user}')
def update_user(id_user, name=None, age=None):
    user_update = session.query(User).filter(User.id == id_user).first()
    if user_update:
        if name:
            user_update.name = name
        if age:
            user_update.age = age
        session.commit()
    else:
        print(f'Usuário: {id_user} não encontrado - Nome: {name}')

# create_user('Carlos', 46)
# create_user('Eduarda', 20)
# update_user(1, 'Carlos Eduardo', 23)
# delete_user(1)
list_users()
