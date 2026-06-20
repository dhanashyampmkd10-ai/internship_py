from fastapi import APIRouter, HTTPException
from schema import Task
from database import (
    create_task,
    get_all_tasks,
    get_tasks_by_status,
    get_task,
    update_task,
    delete_task
)

router = APIRouter()


@router.post("/tasks")
def add_task(task: Task):
    task_id = create_task(task.title, task.status)

    return {
        "id": task_id,
        "title": task.title,
        "status": task.status
    }


@router.get("/tasks")
def read_tasks(status: str = None):
    if status:
        return get_tasks_by_status(status)

    return get_all_tasks()


@router.get("/tasks/{task_id}")
def read_task(task_id: int):
    task = get_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.put("/tasks/{task_id}")
def edit_task(task_id: int, task: Task):
    if not get_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")

    update_task(task_id, task.title, task.status)

    return {"message": "Task updated successfully"}


@router.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    if not get_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")

    delete_task(task_id)

    return {"message": "Task deleted successfully"}