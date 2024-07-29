from http import HTTPStatus

import allure
import pytest

from api_tests.tla.api.endpoints.dispshedule import DispScheduleClient
from api_tests.tla.assertions.base import validate_success_response
from api_tests.tla.routes.query import APIQuery
from api_tests.tla.schemas.response.disp_schedule import (
    DispSheduleFullResponse, DispSheduleAllResponse
)


@pytest.mark.asyncio
class TestDispShedule:
    @allure.title(
        'Получение полного списка дисп.расписаний и краткого списка.'
    )
    @pytest.mark.parametrize(
        'args, expected_schema',
        (
                (APIQuery.ALL, DispSheduleAllResponse),
                (APIQuery.FULL, DispSheduleFullResponse)
        )
    )
    def test_get_disp_schedule(
            self,
            args,
            expected_schema,
            disp_schedule_client: DispScheduleClient
    ):
        """
        Тест проверяет получение диспетчерских расписаний.

        Тест параметризован для проверки двух типов запросов:
        полного списка расписаний (ALL) и краткого списка расписаний (FULL).
        """
        response = disp_schedule_client.get_disp_shedule(ids=args)
        validate_success_response(response, expected_schema)

    @allure.title(
        'Создание дисп.расписаний.'
    )
    def test_create_disp_schedule(
            self,
            disp_schedule_data,
            disp_schedule_client: DispScheduleClient,
    ):
        response = disp_schedule_client.create_disp_shedule(disp_schedule_data)
        print(response.text)
        print(response.request.body)

        assert response.status_code == HTTPStatus.OK
