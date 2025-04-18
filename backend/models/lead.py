from pydantic import BaseModel

class Lead(BaseModel):
    name: str
    address: str
    phone: str | None = None
    email: str | None = None
    website: str | None = None
    rating: float | None = None
