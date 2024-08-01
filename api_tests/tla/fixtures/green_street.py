import allure
import pytest_asyncio

from api_tests.tla.api.endpoints.greenstreet import GreenStreetClient
from api_tests.tla.fixtures.base import create_api_client
from api_tests.tla.routes.path import APIPath


@pytest_asyncio.fixture
@allure.title('API клиент для запросов к /greenstreet.')
async def green_street_client() -> GreenStreetClient:
    return create_api_client(GreenStreetClient, APIPath.GREEN_STREET)
