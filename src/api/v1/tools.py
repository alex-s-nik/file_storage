from fastapi import APIRouter


router = APIRouter()


@router.get(
    '/ping',
    summary='Доступность сервисов'
)
async def get_services_status(

):
    """Проверка доступности сервисов, используемых в проекте"""
    ...
