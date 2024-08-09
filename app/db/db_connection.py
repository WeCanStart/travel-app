import os
import typing
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
passwd = os.getenv("DB_PASSWD")
db_name = "travelRoutes"
usr_name = "root"
conn_str = f"mysql+pymysql://{usr_name}:{passwd}@localhost/{db_name}"


def engine_creation(conn: str):
    return create_engine(conn)


def session_creation(engine):
    return sessionmaker(bind=engine, autoflush=False)


