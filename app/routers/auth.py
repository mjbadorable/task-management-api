from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from .. import schemas, models, database
from ..security.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_password = hash_password(user.password)

    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    # FIX 1: Access the .username property of the form
    db_user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not db_user:
        # FIX 2: Use 401 for both to stay secure
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    # FIX 3: Correct variable mapping
    if not verify_password(user_credentials.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(data={"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer",
    }