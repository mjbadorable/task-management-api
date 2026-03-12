from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, schemas, database
router = APIRouter()

def get_db():
    db = database.SessionLocal()  # New session per request
    try:
        yield db  # Pass to endpoint, keep open
    finally:
        db.close() # Always close after response

@router.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@router.post("/tasks")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task.title)

