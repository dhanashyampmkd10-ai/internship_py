from fastapi import FastAPI
from routers.tasks import router
from database import create_table

app = FastAPI()

create_table()

app.include_router(router)