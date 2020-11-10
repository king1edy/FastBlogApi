from sqlalchemy import Column, Integer, String
from .database import Base


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String,)
    last_name = Column(String)
    age = Column(Integer)


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
