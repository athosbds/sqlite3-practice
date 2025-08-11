from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import User, session

def create_user(name, age):
    new = User(name=name, age=age)
    session.add(new)
    session.commit()

def show_users(): # terminar pra mostrar usuários

def update_user(usuario_id, new_name=None, new_age=None): # terminar aqui atualizar


def delete_user(user_id): # deletar usuário
