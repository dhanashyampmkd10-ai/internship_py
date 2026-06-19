from fastapi import APIRouter, HTTPException, Depends
from database import get_connection
from schemas import UserCreate, UserLogin
from auth import create_token, get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserCreate):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users(email,password) VALUES (?,?)",
            (user.email, user.password)
        )
        conn.commit()

        return {"message": "User registered"}

    except:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


@router.post("/login")
def login(user: UserLogin):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (user.email, user.password)
    )

    db_user = cur.fetchone()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_token(user.email)

    return {
        "access_token": token
    }


@router.get("/me")
def me(email=Depends(get_current_user)):
    return {
        "email": email
    }