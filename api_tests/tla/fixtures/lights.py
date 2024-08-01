import allure
import pytest_asyncio

from api_tests.tla.api.endpoints.lights import LightsClient
from api_tests.tla.fixtures.base import create_api_client
from api_tests.tla.routes.path import APIPath


@pytest_asyncio.fixture
@allure.title('API клиент для запросов к /lights.')
async def lights_client() -> LightsClient:
    return create_api_client(LightsClient, APIPath.LIGHTS)
