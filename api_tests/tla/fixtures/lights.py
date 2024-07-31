import allure
import pytest_asyncio

from api_tests.tla.api.api_client import client_api
from api_tests.tla.api.endpoints.lights import LightsClient
from api_tests.tla.routes.path import APIPath
from api_tests.tla.routes.query import APIQuery


@pytest_asyncio.fixture
@allure.title('API клиент для запросов к /lights.')
async def lights_client() -> LightsClient:
    return LightsClient(
        client=client_api(),
        path=APIPath.LIGHTS,
        base_params={
            APIQuery.MSOURCE: APIQuery.BACKMEGAPOLISURL,
        }
    )



