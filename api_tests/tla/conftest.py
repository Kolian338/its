import allure
import pytest_asyncio

from api_tests.tla.api.api_client import client_api
from api_tests.tla.api.lights import LightsClient
from core.db import AsyncSessionPg


@pytest_asyncio.fixture
@allure.title('API клиент для запросов к /lights')
def lights_client():
    return LightsClient(
        client=client_api()
    )


@allure.title('Создается асинхронный генератор сессий')
@pytest_asyncio.fixture
async def get_async_session():
    async with AsyncSessionPg() as async_session:
        yield async_session
