import allure
import pytest

from api_tests.tla.api.endpoints.greenstreet import GreenStreetClient
from api_tests.tla.assertions.base import (
    validate_response,
)
from api_tests.tla.routes.query import APIQuery
from api_tests.tla.schemas.response.green_street import (
    GreenStreetFullResponse, GreenStreetAllResponse
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
