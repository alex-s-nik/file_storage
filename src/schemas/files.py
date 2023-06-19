from datetime import datetime

from pydantic import BaseModel, UUID4


class FileInDB(BaseModel):
    id: UUID4
    name: str
    created_at: datetime
    path: str
    size: int
    is_downloadable: bool

    class Config:
        orm_mode = True


class FileCreate(BaseModel):
    name: str
    path: str
    size: int
    user_id: UUID4

    class Config:
        orm_mode = True
