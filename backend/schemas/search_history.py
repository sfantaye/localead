from pydantic import BaseModel

class SearchHistoryBase(BaseModel):
    query: str

class SearchHistoryCreate(SearchHistoryBase):
    pass

class SearchHistory(SearchHistoryBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
