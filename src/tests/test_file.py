from fastapi import status
from httpx import AsyncClient

from main import app


async def test_unauthorized_file_upload():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/api/v1") as ac:
        response = await ac.post(
            '/files/upload',
            files={'my_text_file.txt': b'12345'},
            data={'path': 'mydir'}
        )
    assert response.status_code == status.HTTP_403_FORBIDDEN


async def test_file_upload(user_client):
    ...


async def test_info_about_uploaded_files(user_client):
    ...


async def test_download_file(user_client):
    ...


async def test_unauthorized_download(user_client):
    ...
