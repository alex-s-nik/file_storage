from fastapi import status
from httpx import AsyncClient

from main import app


async def test_unauthorized_file_upload():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/") as ac:
        response = await ac.post(
            app.url_path_for('files_upload'),
            files={'my_text_file.txt': b'12345'},
            data={'path': 'mydir'}
        )
    assert response.status_code == status.HTTP_403_FORBIDDEN


async def test_file_upload(user_client):
    user_data = {
        'username': 'a@a.com',
        'password': '11111',
    }
    response = await user_client.post(app.url_path_for('auth:jwt.login'), data=user_data)
    token = response.json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}

    files = {'file': b'123123123'}
    data = {
        'path': 'test/',
        'name': 'test_name.txt'
    }

    response = await user_client.post(
        app.url_path_for('upload'),
        headers=headers,
        files=files,
        data=data
    )
    assert response.status_code == status.HTTP_201_CREATED

    response = await user_client.get(
        app.url_path_for('get_info'),
        headers=headers
    )

    assert response.status_code == status.HTTP_200_OK, (
        'Статус запроса информации о загруженных файлах отличается от 200'
    )

    assert len(response.json()) == 1, (
        'В информации о загруженных файлах есть лишние сведения.'
    )
