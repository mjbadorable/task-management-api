from fastapi import FastAPI, APIRouter

router = APIRouter()

tasks = [] # list storing tasks
task_counter = 1  # generates unique IDs

@router.get("/tasks/{task_id}") #API can fetch a specific task
def get_tasks(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return tasks

    return {"error": "Task not found"}
@router.post("/tasks")
def create_task(title: str):
    global task_counter

    new_task = { # Creates dict with ID, title, completed
        "id": task_counter,
        "title": title,
        "completed": False,
    }

    tasks.append(new_task)
    task_counter += 1
    return new_task

@router.put("/tasks/{task_id}")
def update_task(task_id: int, title: str, completed: bool):

    for task in tasks: #Loop through your tasks list
        if task["id"] == task_id: # Found matching ID?
            task["title"] = title # Update title
            task["completed"] = completed # Update status
            return task # Send back updated task

    return {"error": "Task not found"}

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}

    return {"error": "Task not found"}