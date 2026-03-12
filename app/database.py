from sqlalchemy import create_engine #makes the database connection
from sqlalchemy.orm import sessionmaker #creates database "sessions"
from sqlalchemy.orm import declarative_base #creates parent class for your Task model

DATABASE_URL = "sqlite:///tasks.db" #Connection string telling SQLAlchemy to use SQLite

engine = create_engine( #Creates the database "engine"
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()