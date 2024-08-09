from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase): pass


class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    nickname = Column(String, nullable=False, unique=True)
    user_password = Column(String, nullable=False)
    email = Column(String, nullable=True)

