from fastapi.testclient import TestClient
from app.database import get_db, Base
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import pytest
load_dotenv()


SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql",
    username=os.getenv('DB_USER_TEST'),
    password=os.getenv('DB_PASSWORD_TEST'),
    host=os.getenv('DB_HOST_TEST'),
    database=os.getenv('DB_NAME_TEST'),
    port= 5432
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)  #create connection to database
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # to use session in other files


@pytest.fixture(scope="module")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="module")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    
