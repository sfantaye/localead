from typing import Optional
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.manager import BaseUserManager
from fastapi_users import schemas
from backend.models.user import User
from backend.database import get_async_session
from backend.config import SECRET_KEY

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

class UserManager(BaseUserManager[User, int]):
    user_db_model = User
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request=None):
        print(f"User {user.email} has registered.")

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
