import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routers.auth_router import router as auth_router
from routers.tasks_router import router as task_router

app = FastAPI()

init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    print(f"{request.method} {request.url.path} {duration:.3f}s")

    return response


app.include_router(auth_router)
app.include_router(task_router)