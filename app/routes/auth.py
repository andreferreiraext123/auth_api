# filepath: app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.services.auth_service import hash_password

router = APIRouter()

@router.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.SessionLocal)):
    hashed_password = hash_password(user.password)
    db_user = models.user.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# The code above is a FastAPI route for user registration. It defines an endpoint `/register` that accepts a POST request with user details.
# The route uses Pydantic schemas to validate the incoming data and SQLAlchemy for database interactions.       
