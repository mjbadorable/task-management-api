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

@router.get("/tasks/{task_id}")
def read_tasks(task_id: int, db: Session = Depends(get_db)):
    return crud.get_tasks(db, task_id)

@router.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task.title)

@router.put("/tasks/{task_id}")
def update_task(task_id: int, title: str, completed: bool, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, title, completed)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)

