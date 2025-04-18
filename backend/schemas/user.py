from typing import Optional
from pydantic import EmailStr
from fastapi_users import schemas
from uuid import UUID


class UserRead(schemas.BaseUser[UUID]):
    id: UUID
    email: EmailStr
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str


class UserUpdate(schemas.BaseUserUpdate):
    pass