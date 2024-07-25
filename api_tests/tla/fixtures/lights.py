import allure
import pytest_asyncio
import pytest

from api_tests.tla.api.api_client import client_api
from api_tests.tla.api.endpoints.lights import LightsClient
from core.db import AsyncSessionPg


@pytest_asyncio.fixture
@allure.title('API клиент для запросов к /lights.')
async def lights_client() -> LightsClient:
    return LightsClient(
        client=client_api()
    )


@allure.title('Создается асинхронный генератор сессий.')
@pytest_asyncio.fixture
async def get_async_session():
    async with AsyncSessionPg() as async_session:
        yield async_session
