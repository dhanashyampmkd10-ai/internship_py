from fastapi import FastAPI
from database import init_db, create_task
from model import Task

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.post("/tasks")
def add_task(task: Task):
    return create_task(task)
