from fastapi import APIRouter, HTTPException
from schemas import TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

tasks_db = {}
task_id = 1


@router.get("/")
def get_tasks():
    return list(tasks_db.values())


@router.get("/{id}")
def get_task(id: int):
    if id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[id]


@router.post("/")
def create_task(task: TaskCreate):
    global task_id

    new_task = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks_db[task_id] = new_task
    task_id += 1

    return new_task


@router.put("/{id}")
def update_task(id: int, task: TaskUpdate):
    if id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks_db[id] = {
        "id": id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    return tasks_db[id]


@router.delete("/{id}")
def delete_task(id: int):
    if id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted = tasks_db.pop(id)
    return {"message": "Task deleted", "task": deleted}


# Bonus
@router.patch("/{id}/complete")
def complete_task(id: int):
    if id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks_db[id]["completed"] = True
    return tasks_db[id]