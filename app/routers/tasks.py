from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi import HTTPException

from .. import crud, schemas, database
router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

def get_db():
    db = database.SessionLocal()  # New session per request
    try:
        yield db  # Pass to endpoint, keep open
    finally:
        db.close() # Always close after response

@router.get("/{task_id}")
def read_tasks(task_id: int, db: Session = Depends(get_db)):

    task = crud.get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

@router.post("/")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = crud.create_task(db, task.title)

    return {
        "success": True,
        "data": new_task
    }

@router.put("/tasks/{task_id}")
def update_task(task_id: int, title: str, completed: bool, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, title, completed)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = crud.delete_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
