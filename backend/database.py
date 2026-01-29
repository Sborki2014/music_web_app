from sqlalchemy import create_engine # Нужна для подключения к БД
from sqlalchemy.ext.declarative import declarative_base # ???
from sqlalchemy.orm import sessionmaker # ???

SQL_DB_URL = 'sqlite:///./itproger.db'

engine = create_engine(SQL_DB_URL, connect_args={'check_same_thread': False}) # SQLITE имеет ограничение к подключения из различных потоков, поэтому мы его отключаем (false)

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base() # Она создаёт базовый класс из моделей из которых будут созданны таблицы