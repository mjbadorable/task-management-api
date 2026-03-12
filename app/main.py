from fastapi import FastAPI
from .routers import tasks
from .database import engine
from .models import Base
from .routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="A REST API for managing tasks built with FastAPI and SQLAlchemy",
    version="1.0.0"
)

app.include_router(tasks.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "Task Management API is running"}