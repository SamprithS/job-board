# backend/app/routes/auth.py
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db  # we will add get_db helper in database.py if missing
from app import models, schemas
from app.core.security import get_password_hash, verify_password, create_access_token
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.UserOut)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db_session)):
    existing = db.query(models.User).filter(models.User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = get_password_hash(user_in.password)
    user = models.User(email=user_in.email, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Login endpoint that accepts JSON (email/password)
@router.post("/login", response_model=schemas.Token)
def login(form_data: dict, db: Session = Depends(get_db_session)):
    """
    Accepts JSON body: {"email":"you@example.com","password":"..."}
    (We also accept OAuth2 form data if you prefer.)
    """
    # if called from OAuth2PasswordRequestForm, handle that:
    if isinstance(form_data, OAuth2PasswordRequestForm):
        username = form_data.username
        password = form_data.password
    else:
        username = form_data.get("email")
        password = form_data.get("password")

    if not username or not password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email and password required")

    user = db.query(models.User).filter(models.User.email == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")

    access_token_expires = timedelta(minutes=int(__import__("os").environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 60)))
    token = create_access_token({"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer"}
