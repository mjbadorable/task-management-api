from fastapi import FastAPI, APIRouter

router = APIRouter()

tasks = []

@router.get("/tasks")
def get_tasks():
    return tasks

@router.post("/tasks")
def create_task(task: str):
    tasks.append(task)
    return {"task_added": task}