from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Temporary storage
users = {}


class UserRequest(BaseModel):
    email: str
    password: str


# Register
@router.post("/register")
def register(user: UserRequest):

    if user.email in users:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    users[user.email] = user.password

    return {
        "message": "Registration successful"
    }


# Login
@router.post("/login")
def login(user: UserRequest):

    if user.email not in users:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if users[user.email] != user.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "access_token": "dummy_token"
    }