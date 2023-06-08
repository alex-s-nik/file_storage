import uuid
from datetime import datetime

from pydantic import BaseModel


class FileInDB(BaseModel):
    id: uuid.uuid4
    name: str
    created_at: datetime
    path: str
    size: int
    is_downloadable: bool
    