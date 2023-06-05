from fastapi import APIRouter, Response, status


from services.tools import services_status

router = APIRouter()

@router.get(
    '/ping',
    summary='Доступность сервисов'
)
async def get_services_status(

):
    """Проверка доступности сервисов, используемых в проекте"""
    ...
