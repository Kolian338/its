import allure
import pytest

from api_tests.tla.api.endpoints.greenstreet import GreenStreetClient
from api_tests.tla.assertions.base import validate_response
from api_tests.tla.fixtures.base import create_api_client
from api_tests.tla.routes.path import APIPath
from api_tests.tla.schemas.request.green_street import (
    AddGreenPartRequest, AddGreenRouteRequest
)
from api_tests.tla.schemas.response.green_street import GreenPartResponse


@pytest.fixture
@allure.title('API клиент для запросов к /greenstreet.')
def green_street_client() -> GreenStreetClient:
    return create_api_client(GreenStreetClient, APIPath.GREEN_STREET)


@pytest.fixture
@allure.title('Создаение объекта участка зеленой улицы.')
def green_street_part_data() -> AddGreenPartRequest:
    return AddGreenPartRequest()


@pytest.fixture
@allure.title('Создаение объекта маршрута зеленой улицы.')
def green_street_rout_data() -> AddGreenRouteRequest:
    return AddGreenRouteRequest()


@pytest.fixture
@allure.title('Создаение участка в API.')
def create_green_street_part(
        green_street_client: GreenStreetClient,
        green_street_part_data: AddGreenPartRequest
) -> GreenPartResponse:
    response = green_street_client.create_part(
        payload=green_street_part_data
    )
    validated_part = validate_response(
        response, GreenPartResponse
    )
    return validated_part
