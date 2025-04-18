from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from backend.auth import auth_backend, get_user_manager
from backend.models.user import User  # assuming User is in models/user.py
from backend.schemas.user import UserRead, UserCreate  # adjust if needed

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router = APIRouter()

# Register routes
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserCreate),
    prefix="/users",
    tags=["users"],
)
