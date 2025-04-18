from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.cruds import search_history as crud
from backend.schemas import search_history as schemas
from backend.database import SessionLocal
from backend.models import SearchHistory
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy
from backend.auth import fastapi_users 
from backend.models.user import User
# Ensure it's imported


router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Search History
@router.post("/search-history/", response_model=schemas.SearchHistory)
def create_search_history(
    search_history: schemas.SearchHistoryCreate, 
    db: Session = Depends(get_db),
    user: User = Depends(fastapi_users.current_user),
):
    return crud.create_search_history(db=db, search_history=search_history, user_id=user.id)

# Get Search History for a User
@router.get("/search-history/{user_id}", response_model=list[schemas.SearchHistory])
def read_search_history(
    user_id: int, 
    db: Session = Depends(get_db), 
    skip: int = 0, limit: int = 10
):
    search_history = crud.get_search_history_by_user(db=db, user_id=user_id, skip=skip, limit=limit)
    if not search_history:
        raise HTTPException(status_code=404, detail="Search history not found")
    return search_history

# Get a Single Search History Record by ID
@router.get("/search-history/{search_history_id}", response_model=schemas.SearchHistory)
def read_search_history_by_id(
    search_history_id: int, 
    db: Session = Depends(get_db)
):
    search_history = crud.get_search_history(db=db, search_history_id=search_history_id)
    if not search_history:
        raise HTTPException(status_code=404, detail="Search history not found")
    return search_history
