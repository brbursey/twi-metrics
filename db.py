import os

import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
hostname = os.getenv("HOSTNAME")
name = os.getenv("POSTGRES_DB")

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{hostname}/{name}")
Session = sessionmaker(bind=engine)
