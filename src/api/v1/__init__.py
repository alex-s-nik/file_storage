from fastapi import APIRouter

from .files import router as file_router
from .tools import router as tools_router
from .users import router as user_router

router = APIRouter()

router.include_router(file_router, prefix='/files')
router.include_router(tools_router)
router.include_router(user_router)
