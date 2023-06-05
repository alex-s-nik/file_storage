from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.user import auth_backend, current_user, fastapi_users
from db.db import get_async_session
from models.users import User
from schemas.users import UserCreate, UserRead, UserUpdate


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)
