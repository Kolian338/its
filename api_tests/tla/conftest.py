import allure
import pytest

from api_tests.tla.api.api_client import client_api
from api_tests.tla.api.lights import LightsClient


@pytest.fixture()
@allure.title('API клиент для запросов к /lights')
def lights_client():
    return LightsClient(
        client=client_api()
    )
