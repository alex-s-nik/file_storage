from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession

from core.user import current_user
from db.db import get_async_session
from models.users import User
from services.files import get_file_path_name, get_files_info, upload_file_to_service
from schemas.files import FileInDB

router = APIRouter()


@router.get(
    '',
    summary='Информация о загруженных файлах',
    dependencies=[Depends(current_user)]
)
async def get_info(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
) -> List[FileInDB]:
    """Получить информацию о загруженных файлах пользователя"""
    return (await get_files_info(user, session))


@router.post(
    '/upload',
    summary='Загрузить файл',
    dependencies=[Depends(current_user)]
)
async def files_upload(
    path: str,
    file: UploadFile = File(...),
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Загрузить файлы в сервис"""
    try:
        await upload_file_to_service(path, file, user, session)
    except Exception as e:
        raise HTTPException(
            status_code=403,
            detail={"message": f"There was an error uploading the file - {e}"}
        )

    return {"message": f"Successfuly uploaded {file.filename}"}


@router.get(
    '/download',
    summary='Скачать файлы',
    dependencies=[Depends(current_user)]
)
async def files_download(
    path: str,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Скачивание файлов с помощью сервиса"""
    path_to_file, filename = get_file_path_name(path, user)
    return FileResponse(path=path_to_file, filename=filename)
