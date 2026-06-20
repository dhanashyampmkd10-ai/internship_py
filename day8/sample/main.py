from fastapi import FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext
import sqlite3

# Create FastAPI app
app = FastAPI()

# Connect to SQLite database
conn = sqlite3.connect(
    "app.db",
    check_same_thread=False
)

db = conn.cursor()

# Create users table
db.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    hashed_password TEXT
)
""")

conn.commit()

# Password hashing object
pwd_context = CryptContext(
    schemes=["bcrypt"]
)

# Request model
class UserCreate(BaseModel):
    email: str
    password: str


# Register endpoint
@app.post("/auth/register")
def register(user: UserCreate):

    # Check if email already exists
    existing_user = db.execute(
        """
        SELECT * FROM users
        WHERE email = ?
        """,
        (user.email,)
    ).fetchone()

    if existing_user:
        return {
            "message": "Email already exists"
        }

    # Hash password
    hashed_password = pwd_context.hash(
        user.password
    )

    # Save user
    db.execute(
        """
        INSERT INTO users(
            email,
            hashed_password
        )
        VALUES (?, ?)
        """,
        (
            user.email,
            hashed_password
        )
    )

    conn.commit()

    return {
        "message": "User created successfully"
    }


# Home route
@app.get("/")
def home():
    return {
        "message": "FastAPI is working"
    }