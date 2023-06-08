from typing import List

from fastapi import APIRouter, Depends, File, Response, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from core.user import current_user
from db.db import get_async_session
from models.users import User
from services.files import get_files_info, upload_file_to_service
from schemas.files import FileInDB

router = APIRouter()


@router.get(
    '',
    summary='Информация о загруженных файлах'
)
async def get_info(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
) -> List[FileInDB]:
    """Получить информацию о загруженных файлах пользователя"""
    return (await get_files_info(user, session))

@router.post(
    '/upload',
    summary='Загрузить файл'
)
async def files_upload(
    file: UploadFile = File(...),
    session: AsyncSession = Depends(get_async_session)
):
    """Загрузить файлы в сервис"""
    try:
        upload_file_to_service(file, session)
    except Exception:
        return {"message": "There was an error uploading the file"}

    return {"message": f"Successfuly uploaded {file.filename}"}


@router.get(
    '/download',
    summary='Скачать файлы'
)
async def files_download():
    """Скачивание файлов с помощью сервиса"""
    return Response('This is download route')

