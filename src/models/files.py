import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from db.db import BaseModel
from .users import User


class File(BaseModel):
    __tablename__ = 'files'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    # Здесь только путь до файла без его имени
    # Таим образом путь может быть одинаковый у разных файлов
    # Далее в сервисе путь и имя файла соединяются в абсолютный путь.
    # Улучшение вижу в отказе от id и вводе составного первичного ключа
    # из двух полей - пути и имени файла, либо
    # оставить id и ввести unique constraint по пути и имени файла.
    # Реализовал второй вариант.
    path = Column(Text, nullable=False)
    size = Column(Integer, nullable=False)
    is_downloadable = Column(Boolean, default=True, nullable=False)
    user_id = Column(UUID, ForeignKey(User.id, ondelete="CASCADE"))

    UniqueConstraint(name, path, name='unique_filename')
