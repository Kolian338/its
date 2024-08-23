import allure
import pytest
from assertpy import assert_that

from api_tests.tla.api.endpoints.greenstreet import GreenStreetClient
from api_tests.tla.assertions.base import (
    validate_response,
)
from api_tests.tla.helper.green_street import update_route_with_part_guid
from api_tests.tla.routes.query import APIQuery
from api_tests.tla.schemas.request.green_street import (
    AddGreenRouteRequest
)
from api_tests.tla.schemas.response.green_street import (
    GreenStreetFullResponse, GreenStreetAllResponse, GreenPartResponse,
    GreenRoutResponse, GreenPartOrRouteDeleteResponse
)


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
    def test_green_street_create_part(
            self,
            create_part_and_delete_after: GreenPartResponse,
            get_green_street_all: GreenStreetAllResponse,
    ):
        """
        Тест проверяет создание участка зеленой улицы и его присутствие
         в списке зеленых улиц.
        """
        guid_from_current_part = (
            create_part_and_delete_after.get_guids()[0]
        )
        assert_that(
            guid_from_current_part
        ).is_in(*get_green_street_all.get_guids_from_parts())

    @allure.title(
        'Удаление участка ЗУ.'
    )
    def test_green_street_delete_part(
            self,
            green_street_client: GreenStreetClient,
            create_part_without_delete: GreenPartResponse
    ):
        """
        Проверяет удаление участка зеленой улицы по его GUID.

        :param green_street_client: API клиент для взаимодействия
         с зелеными улицами.
        :param create_part_without_delete: Созданный участок для удаления.
        """
        guid_from_current_part = (
            create_part_without_delete.get_guids()[0]
        )
        response = green_street_client.delete_part(guid_from_current_part)
        validate_response(
            response, GreenPartOrRouteDeleteResponse
        )

    @allure.title(
        'Создание только маршрута ЗУ.'
    )
    def test_green_street_create_route(
            self,
            create_green_street_route_and_delete: GreenRoutResponse,
            get_green_street_all: GreenStreetAllResponse,
    ):
        """
        Тест проверяет создание маршрута зеленой улицы и проверяет его наличие
        в списке всех маршрутов.
        """
        guid_from_current_route = (
            create_green_street_route_and_delete.get_guids()[0]
        )
        assert_that(
            guid_from_current_route
        ).is_in(*get_green_street_all.get_guids_from_routes())

    @allure.title(
        'Создание маршрута с участком, ЗУ.'
    )
    def test_green_street_create_route_with_parts(
            self,
            green_street_rout_data: AddGreenRouteRequest,
            green_street_client: GreenStreetClient,
            create_part_and_delete_after: GreenPartResponse
    ):
        update_route_with_part_guid(
            green_street_rout_data,
            create_part_and_delete_after.info[0].guid
        )
        response = green_street_client.create_route(
            payload=green_street_rout_data
        )
        validate_response(
            response, GreenRoutResponse
        )
