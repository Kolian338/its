import allure
import pytest

from api_tests.tla.api.endpoints.greenstreet import GreenStreetClient
from api_tests.tla.assertions.base import (
    validate_response,
)
from api_tests.tla.helper.green_street import update_route_with_part_guid
from api_tests.tla.routes.query import APIQuery
from api_tests.tla.schemas.request.green_street import (
    AddGreenPartRequest, AddGreenRouteRequest
)
from api_tests.tla.schemas.response.green_street import (
    GreenStreetFullResponse, GreenStreetAllResponse, GreenPartResponse,
    GreenRoutResponse
)


@pytest.mark.asyncio
class TestGreenStreet:
    @allure.title(
        'Получение списка участков и маршрутов Зеленых улиц.'
    )
    @pytest.mark.parametrize(
        'args, expected_schema',
        (
                (APIQuery.ALL, GreenStreetAllResponse),
                (APIQuery.FULL, GreenStreetFullResponse)
        )
    )
    def test_get_green_street(
            self,
            args,
            expected_schema,
            green_street_client: GreenStreetClient
    ):
        """
        Тест проверяет получение зеленых улиц.

        Тест параметризован для проверки двух типов запросов:
        полного списка (ALL) и краткого списка (FULL).
        """
        response = green_street_client.get_green_street(ids=args)
        validate_response(response, expected_schema)

    @allure.title(
        'Создание только участка ЗУ.'
    )
    def test_green_street_create_parts(
            self,
            green_street_part_data: AddGreenPartRequest,
            green_street_client: GreenStreetClient,
    ):
        response = green_street_client.create_part(
            payload=green_street_part_data
        )
        validate_response(
            response, GreenPartResponse
        )

    @allure.title(
        'Создание только маршрута ЗУ.'
    )
    def test_green_street_create_route(
            self,
            green_street_rout_data: AddGreenRouteRequest,
            green_street_client: GreenStreetClient,
    ):
        response = green_street_client.create_route(
            payload=green_street_rout_data
        )
        validate_response(
            response, GreenRoutResponse
        )

    @allure.title(
        'Создание маршрута с участком, ЗУ.'
    )
    def test_green_street_create_route_with_parts(
            self,
            green_street_rout_data: AddGreenRouteRequest,
            green_street_client: GreenStreetClient,
            create_green_street_part: GreenPartResponse
    ):
        update_route_with_part_guid(
            green_street_rout_data, create_green_street_part.info[0].guid
        )
        response = green_street_client.create_route(
            payload=green_street_rout_data
        )
        validate_response(
            response, GreenRoutResponse
        )
