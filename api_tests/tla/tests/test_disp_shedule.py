from http import HTTPStatus

import allure
import pytest

from api_tests.tla.api.endpoints.dispshedule import DispScheduleClient


@pytest.mark.asyncio
class TestDispShedule:
    @allure.title(
        'Тесты дисп.расписаний.'
    )
    # @pytest.mark.parametrize(
    #     'id',
    #     (4098, [4098])
    # )
    def test_create_disp_schedule(
            self,
            disp_schedule_data,
            disp_schedule_client: DispScheduleClient,
    ):
        response = disp_schedule_client.create_disp_shedule(disp_schedule_data)
        print(response.text)
        print(response.request.body)

        assert response.status_code == HTTPStatus.OK
