from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()


SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql",
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    database=os.getenv('DB_NAME'),
    port= 5432
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)  #create connection to database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # to use session in other files
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




