import allure
import pytest_asyncio
from requests import Response

from api_tests.tla.api.api_client import client_api
from api_tests.tla.api.endpoints.lights import LightsClient
from api_tests.tla.assertions.schema import validate_schema
from api_tests.tla.schemas.lights import LightStateResponse
from core.db import AsyncSessionPg


@pytest_asyncio.fixture
@allure.title('API клиент для запросов к /lights.')
async def lights_client() -> LightsClient:
    return LightsClient(
        client=client_api()
    )


@pytest_asyncio.fixture
@allure.title('Получение состояния СО по id.')
async def get_lights_by_id_response(
        lights_client: LightsClient, request
) -> Response:
    id = request.param
    response = lights_client.get_lights_state_by_id(id)
    validate_schema(
        response.json(), LightStateResponse.model_json_schema()
    )
    return response


@pytest_asyncio.fixture
@allure.title('Получение списка СО по ids.')
async def get_lights_state_by_ids_response(
        lights_client: LightsClient, request
) -> Response:
    response = lights_client.get_lights_state_by_ids()
    validate_schema(
        response.json(), LightStateResponse.model_json_schema()
    )
    return response


@allure.title('Создается асинхронный генератор сессий.')
@pytest_asyncio.fixture
async def get_async_session():
    async with AsyncSessionPg() as async_session:
        yield async_session
