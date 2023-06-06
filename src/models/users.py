from sqlalchemy import Column, Integer
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from db.db import BaseModel


class User(SQLAlchemyBaseUserTableUUID, BaseModel):
    pass
