from http import HTTPStatus

import allure
import pytest
from requests import Response

from api_tests.tla.crud.lights import (
    traffic_lights_objects
)
from api_tests.tla.schemas.lights import LightStateResponse


@allure.feature('Lights')
@allure.story('Lights API')
class TestLightsState:
    @allure.title(
        'Получение состояния одного/нескольких светофорных объектов.'
    )
    @pytest.mark.parametrize(
        'get_lights_by_id_response',
        (4097, 4098, [4097, 4098]),
        indirect=True
    )
    def test_get_light_state(
            self,
            get_lights_by_id_response: Response,
    ) -> None:
        LightStateResponse(**get_lights_by_id_response.json())
        assert get_lights_by_id_response.status_code == HTTPStatus.OK

    @allure.title(
        'Получение состояния списка светофорных объектов.'
    )
    def test_get_all_lights(
            self,
            get_lights_state_by_ids_response
    ) -> None:
        LightStateResponse(**get_lights_state_by_ids_response.json())
        assert get_lights_state_by_ids_response.status_code == HTTPStatus.OK


# Для тестов к БД
@pytest.mark.asyncio
async def test_async_function(get_async_session):
    obj_db = await traffic_lights_objects.get_by_attribute(
        'ext_id',
        '4097',
        get_async_session
    )
    objects_db = await traffic_lights_objects.get_multi(get_async_session)
    print(obj_db.ext_id)
    print(objects_db)
