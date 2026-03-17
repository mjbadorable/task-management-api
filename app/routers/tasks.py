from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database
from ..models import User
from ..security.dependencies import get_current_user

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

@router.get("/")
def read_tasks(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):

    return db.query(models.Task).filter(models.Task.owner_id == current_user.id).all()

@router.post("/")
def create_task(
    task: schemas.TasksCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_task = models.Task(
        title=task.title,
        owner_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.put("/tasks/{task_id}")
def update_task(task_id: int, title: str, completed: bool, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, title, completed)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = crud.delete_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
