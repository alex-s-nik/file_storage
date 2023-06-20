import asyncio

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from main import app
from models import User
from core.config import app_settings
from core.user import current_user
from db.db import BaseModel, get_async_session

user = User()


engine = create_async_engine(app_settings.test_database_dsn, echo=True, future=True)
test_async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_test_async_session() -> AsyncSession:
    async with test_async_session() as session:
        yield session


app.dependency_overrides = {}
app.dependency_overrides[current_user] = lambda: user
app.dependency_overrides[get_async_session] = get_test_async_session


@pytest.fixture()
def user_client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(autouse=True)
def test_db():
    BaseModel.metadata.create_all(bind=engine)
    yield
    BaseModel.metadata.drop_all(bind=engine)


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
