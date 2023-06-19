from logging import config as logging_config
from pathlib import Path

from pydantic import BaseSettings, Field, PostgresDsn

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)

BASE_DIR = Path(__file__)

UPLOAD_DIR = BASE_DIR.parent / 'uploads'

print(BASE_DIR.parent.parent.parent / '.env')
print(Path(__file__).cwd())


class AppSettings(BaseSettings):
    app_title: str = "FileShareApp"
    postgres_dsn: PostgresDsn
    engine_echo: bool = Field(True, env='ENGINE_ECHO')
    project_name: str = Field('file_uploader', env='PROJECT_NAME')
    project_host: str = Field('0.0.0.0', env='PROJECT_HOST')
    project_port: int = Field(8000, env='PROJECT_PORT')
    secret: str = 'SECRET_WORD'

    class Config:
        env_file = BASE_DIR.parent.parent.parent / '.env'


app_settings = AppSettings()
