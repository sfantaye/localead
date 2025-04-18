from sqlalchemy.orm import Session
from backend.models import SearchHistory, User
from backend.schemas.search_history import SearchHistoryCreate

# Create Search History
def create_search_history(db: Session, search_history: SearchHistoryCreate, user_id: int):
    db_search_history = SearchHistory(query=search_history.query, user_id=user_id)
    db.add(db_search_history)
    db.commit()
    db.refresh(db_search_history)
    return db_search_history

# Get Search History by User
def get_search_history_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(SearchHistory).filter(SearchHistory.user_id == user_id).offset(skip).limit(limit).all()

# Get Search History by ID
def get_search_history(db: Session, search_history_id: int):
    return db.query(SearchHistory).filter(SearchHistory.id == search_history_id).first()
