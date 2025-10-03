# backend/app/routes/auth.py
from fastapi import APIRouter, HTTPException, status, Depends, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.core.security import get_password_hash, verify_password, create_access_token
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
import os

router = APIRouter()


@router.post("/register", response_model=schemas.UserOut, tags=["auth"])
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = get_password_hash(user_in.password)
    # user_in.role is a UserRole enum from Pydantic
    user = models.User(email=user_in.email, hashed_password=hashed, role=user_in.role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=schemas.Token, tags=["auth"])
def login(form_data: dict, db: Session = Depends(get_db)):
    """
    Accepts JSON body: {"email":"you@example.com","password":"..."}
    """
    # Handle both OAuth2 form and JSON
    if isinstance(form_data, OAuth2PasswordRequestForm):
        username = form_data.username
        password = form_data.password
    else:
        username = form_data.get("email")
        password = form_data.get("password")

    if not username or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email and password required",
        )

    user = db.query(models.User).filter(models.User.email == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials"
        )

    access_token_expires = timedelta(
        minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    )
    token = create_access_token({"sub": user.email}, expires_delta=access_token_expires)

    return {"access_token": token, "token_type": "bearer"}


@router.post("/logout", tags=["auth"])
def logout(request: Request, db: Session = Depends(get_db)):
    """Logout endpoint - revokes the current token"""
    # Extract Authorization header
    auth = request.headers.get("authorization")
    if not auth:
        raise HTTPException(status_code=400, detail="Authorization header missing")
    if not auth.lower().startswith("bearer "):
        raise HTTPException(status_code=400, detail="Invalid authorization header")

    token = auth.split(" ", 1)[1].strip()

    # Check if already revoked
    existing = (
        db.query(models.RevokedToken).filter(models.RevokedToken.token == token).first()
    )
    if existing:
        return {"msg": "already logged out"}

    # Store token in revoked table
    revoked = models.RevokedToken(token=token)
    db.add(revoked)
    db.commit()

    return {"msg": "logged out successfully"}
