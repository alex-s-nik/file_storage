import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from db.db import BaseModel
from .users import User


class File(BaseModel):
    __tablename__ = 'files'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now, nullable=False)
    path = Column(Text, nullable=False)
    size = Column(Integer, nullable=False)
    is_downloadable = Column(Boolean, default=True, nullable=False)
    user_id = Column(UUID, ForeignKey(User.id, ondelete="CASCADE"))
