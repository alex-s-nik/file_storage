from fastapi import APIRouter

router = APIRouter()  # prefix will be 'files'


@router.get(
    '',
    summary='Информация о загруженных файлах'
)
async def get_info():
    """Получить информацию о загруженных файлах пользователя"""
    ...

@router.post(
    '/upload',
    summary='Загрузить файл'
)
async def files_upload():
    """Загрузить файлы в сервис"""
    ...

@router.get(
    '/download',
    summary='Скачать файлы'
)
async def files_download():
    """Скачивание файлов с помощью сервиса"""
    ...
