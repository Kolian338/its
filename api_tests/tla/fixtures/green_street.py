import allure
import pytest

from api_tests.tla.api.endpoints.greenstreet import GreenStreetClient
from api_tests.tla.assertions.base import validate_response
from api_tests.tla.fixtures.base import create_api_client
from api_tests.tla.routes.path import APIPath
from api_tests.tla.routes.query import APIQuery
from api_tests.tla.schemas.request.green_street import (
    AddGreenPartRequest, AddGreenRouteRequest
)
from api_tests.tla.schemas.response.green_street import (
    GreenPartResponse, GreenPartOrRouteDeleteResponse, GreenStreetAllResponse,
    GreenRoutResponse
)


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
@allure.title('Создание и удаление участка ЗУ.')
def create_part_and_delete_after(
        green_street_client: GreenStreetClient,
        green_street_part_data: AddGreenPartRequest
) -> GreenPartResponse:
    """
    Фикстура для создания участка зеленой улицы через API.

    :param green_street_client: Клиент для взаимодействия с API.
    :param green_street_part_data: Данные для создания участка.
    :return: Объект GreenPartResponse с информацией о созданном участке.

    Удаляет созданный участок после завершения теста.
    """
    response = green_street_client.create_part(
        payload=green_street_part_data
    )
    validated_part = validate_response(
        response, GreenPartResponse
    )

    yield validated_part

    part_guid = validated_part.info[0].guid
    delete_response = green_street_client.delete_part(guid=part_guid)
    validate_response(delete_response, GreenPartOrRouteDeleteResponse)


@pytest.fixture
@allure.title('Создание и удаление маршрута ЗУ.')
def create_green_street_route_and_delete(
        green_street_client: GreenStreetClient,
        green_street_rout_data: AddGreenRouteRequest
) -> GreenRoutResponse:
    """
    Фикстура для создания маршрута зеленой улицы через API и его удаления
    после завершения теста.

    :param green_street_client: Клиент для взаимодействия с API.
    :param green_street_rout_data: Данные для создания маршрута.
    :return: Объект GreenRoutResponse с информацией о созданном маршруте.
    """
    # Создание маршрута
    response = green_street_client.create_route(payload=green_street_rout_data)
    validated_route = validate_response(response, GreenRoutResponse)

    yield validated_route

    # Удаление маршрута после завершения теста
    route_guid = validated_route.info[0].guid
    delete_response = green_street_client.delete_route(guid=route_guid)
    validate_response(delete_response, GreenPartOrRouteDeleteResponse)


@pytest.fixture
@allure.title('Создание участка в API без удаления.')
def create_part_without_delete(
        green_street_client: GreenStreetClient,
        green_street_part_data: AddGreenPartRequest
) -> GreenPartResponse:
    """
    Фикстура для создания участка зеленой улицы через API
     без автоматического удаления.

    :param green_street_client: Клиент для взаимодействия с API.
    :param green_street_part_data: Данные для создания участка.
    :return: Объект GreenPartResponse с информацией о созданном участке.
    """
    response = green_street_client.create_part(
        payload=green_street_part_data
    )
    validated_part = validate_response(
        response, GreenPartResponse
    )
    return validated_part


@pytest.fixture
@allure.title('Получение зеленых улиц (ALL).')
def get_green_street_all(
        green_street_client: GreenStreetClient
) -> GreenStreetAllResponse:
    """
    Фикстура для получения полного списка зеленых улиц через API.

    Эта фикстура выполняет запрос к API для получения
    полного списка зеленых улиц (ALL) и валидирует ответ.

    :param green_street_client: Клиент для взаимодействия с API.
    :return: Ответ от API на запрос получения полного списка зеленых улиц,
             валидированный с использованием схемы GreenStreetAllResponse.
    """
    response = green_street_client.get_green_street(ids=APIQuery.ALL)
    validated_green_street = validate_response(
        response, GreenStreetAllResponse
    )
    return validated_green_street
