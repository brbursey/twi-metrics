from flask import Flask
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    twitter_id = Column(Integer, nullable=False)
    authorized = Column(Boolean, nullable=False)
