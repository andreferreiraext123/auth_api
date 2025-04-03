# filepath: app/models/user.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# whats sqlalchemy used for?
# SQLAlchemy is an Object Relational Mapper (ORM) that provides a set of high-level API to interact with databases using Python objects instead of writing raw SQL queries. It allows developers to define database schemas as Python classes and perform CRUD operations using Python methods. SQLAlchemy abstracts the complexity of database interactions, making it easier to work with databases in Python applications.