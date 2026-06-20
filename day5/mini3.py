from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = {}

class Task(BaseModel):
    title: str

@app.post("/tasks")
def create_task(task: Task):
    task_id = len(tasks) + 1

    tasks[task_id] = {
        "id": task_id,
        "title": task.title
    }

    return tasks[task_id]

@app.get("/tasks")
def get_tasks():
    return list(tasks.values())

@app.delete("/tasks/{id}")
def delete_task(id: int):
    if id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    del tasks[id]

    return {"message": "Task deleted"}