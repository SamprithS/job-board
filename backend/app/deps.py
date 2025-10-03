# backend/app/deps.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.security import decode_access_token
from app.database import get_db
from app import models

# OAuth2 scheme for getting tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# Current user dependency (with revoked token check)
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    # 1. Check if token is revoked
    revoked = (
        db.query(models.RevokedToken).filter(models.RevokedToken.token == token).first()
    )
    if revoked:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has been revoked"
        )

    # 2. Decode token
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

    # 3. Extract user from payload
    email = payload.get("sub")
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload"
        )

    # 4. Lookup user in DB
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found"
        )

    return user


# Role requirement helpers
def require_employer(user: models.User = Depends(get_current_user)):
    """Dependency that requires user to be an employer"""
    if user.role.value != "employer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Employers only"
        )
    return user


def require_job_seeker(user: models.User = Depends(get_current_user)):
    """Dependency that requires user to be a job seeker"""
    if user.role.value != "job_seeker":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Job seekers only"
        )
    return user
