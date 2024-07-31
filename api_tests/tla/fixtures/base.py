import allure
import pytest_asyncio

from core.db import AsyncSessionPg


@allure.title('Создается асинхронный генератор сессий.')
@pytest_asyncio.fixture
async def get_async_session():
    async with AsyncSessionPg() as async_session:
        yield async_session
