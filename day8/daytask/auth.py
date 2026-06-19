from jose import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"

security = HTTPBearer()


def create_token(email):
    return jwt.encode(
        {"email": email},
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload["email"]

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )