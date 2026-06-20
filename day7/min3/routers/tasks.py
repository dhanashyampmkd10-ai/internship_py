from fastapi import APIRouter
from schema import TaskCreate
from database import get_connection

router = APIRouter()

@router.post("/tasks")
def create_task(task: TaskCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (task.title,)
    )

    conn.commit()
    conn.close()

    return {"message": "Task added successfully"}

@router.get("/tasks")
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    conn.close()

    return [
        {"id": row[0], "title": row[1]}
        for row in rows
    ]

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Task deleted successfully"}