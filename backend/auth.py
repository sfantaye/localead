from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from backend.database import get_async_session
from backend.models.user import User
from backend.user_manager import get_user_manager
from backend.schemas.user import UserRead, UserCreate, UserUpdate
from backend.config import SECRET_KEY

# JWT config
SECRET = SECRET_KEY

# Transport
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# JWT strategy
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

# Authentication backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# User DB dependency
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

# FastAPI Users instance
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
