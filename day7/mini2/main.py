from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Task model
class Task(BaseModel):
    title: str
    completed: bool = False


# DB connection
def get_connection():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn


# POST → add task
@app.post("/tasks")
def create_task(task: Task):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, completed) VALUES (?, ?)",
        (task.title, task.completed)
    )

    conn.commit()
    conn.close()

    return {"message": "Task added"}


# GET → retrieve tasks  ⭐ THIS WAS MISSING
@app.get("/tasks")
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    return [dict(row) for row in rows]