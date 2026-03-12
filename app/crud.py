from sqlalchemy.orm import Session
from . import models

def get_tasks(db:Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, title: str):
    task = models.Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task:
        db.delete(task)
        db.commit()

    return  task

def update_task(db:Session, task_id: int, title: str, completed: bool):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task:
        task.title = title
        task.completed = completed
        db.commit()
        db.refresh(task)

    return task