import allure
import pytest

from api_tests.tla.api.endpoints.lights import LightsClient
from api_tests.tla.assertions.base import validate_response
from api_tests.tla.fixtures.base import create_api_client
from api_tests.tla.routes.path import APIPath
from api_tests.tla.schemas.response.lights import LightStateResponse


@pytest.fixture
@allure.title('API клиент для запросов к /lights.')
def lights_client() -> LightsClient:
    return create_api_client(LightsClient, APIPath.LIGHTS)
