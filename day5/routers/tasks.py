from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
router = APIRouter()
tasks = {}
next_id = 1
class TaskCreate(BaseModel):
    title: str
    completed: bool = False
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None
class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
@router.get("/", response_model=list[TaskResponse])
def get_tasks():
    return list(tasks.values())
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return tasks[task_id]
@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    global next_id
    new_task = {
        "id": next_id,
        "title": task.title,
        "completed": task.completed
    }
    tasks[next_id] = new_task
    next_id += 1
    return new_task
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    updated_task = {
        "id": task_id,
        "title": task.title,
        "completed": task.completed
    }
    tasks[task_id] = updated_task
    return updated_task
@router.delete("/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    deleted_task = tasks.pop(task_id)

    return {
        "message": "Task deleted",
        "task": deleted_task
    }
@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    tasks[task_id]["completed"] = True
    return tasks[task_id]