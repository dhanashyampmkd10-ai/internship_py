from fastapi import APIRouter, Depends
from database import get_connection
from schemas import TaskCreate, TaskUpdate
from auth import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/")
def create_task(task: TaskCreate, email=Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tasks(title, owner_email) VALUES (?, ?)",
        (task.title, email)
    )

    conn.commit()
    conn.close()

    return {"message": "Task created"}


@router.get("/")
def get_tasks(email=Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM tasks WHERE owner_email=?",
        (email,)
    )

    tasks = [dict(row) for row in cur.fetchall()]

    conn.close()

    return tasks


@router.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate, email=Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE tasks
        SET title=?, completed=?
        WHERE id=? AND owner_email=?
        """,
        (task.title, int(task.completed), task_id, email)
    )

    conn.commit()
    conn.close()

    return {"message": "Task updated"}


@router.delete("/{task_id}")
def delete_task(task_id: int, email=Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM tasks WHERE id=? AND owner_email=?",
        (task_id, email)
    )

    conn.commit()
    conn.close()

    return {"message": "Task deleted"}