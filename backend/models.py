from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship # Нужен для того, чтобы создать связи между полями
from database import Base # Всё наше подключение

class User(Base):
    __tablename__ = 'users' # Настройка, которая позволяет указать название таблицы

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)


class Post(Base):
    __tablename__ = 'posts' # Настройка, которая позволяет указать название таблицы

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User') # Здесь описывается поле, в которое будет помещаться информация о пользователе ( не только имя)