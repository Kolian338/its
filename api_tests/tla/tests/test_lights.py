from http import HTTPStatus

import allure
import pytest

from api_tests.tla.api.endpoints.lights import LightsClient
from api_tests.tla.api.validators.lights import check_light_object_exist
from api_tests.tla.assertions.schema import validate_schema
from api_tests.tla.crud.lights import (
    traffic_lights_objects
)
from api_tests.tla.schemas.lights import LightStateResponse


@pytest.mark.asyncio
@allure.feature('Lights')
@allure.story('Lights API')
class TestLightsState:
    @allure.title(
        'Получение состояния одного/нескольких светофорных объектов.'
    )
    @pytest.mark.parametrize(
        'ext_id',
        (4098, [4098])
    )
    def test_get_light_state(
            self,
            ext_id: int,
            lights_client: LightsClient,
    ):
        response = lights_client.get_lights_state_by_id(ext_id)
        LightStateResponse(**response.json())
        validate_schema(
            response.json(), LightStateResponse.model_json_schema()
        )

        assert response.status_code == HTTPStatus.OK

    @allure.title(
        'Получение состояния списка светофорных объектов.'
    )
    def test_get_all_lights(
            self,
            lights_client: LightsClient,
    ):
        response = lights_client.get_lights_state_by_ids()
        LightStateResponse(**response.json())
        validate_schema(
            response.json(), LightStateResponse.model_json_schema()
        )
        assert response.status_code == HTTPStatus.OK


# Для тестов к БД
@pytest.mark.asyncio
async def test_async_function(get_async_session):
    obj_db = await traffic_lights_objects.get_by_attribute(
        'ext_id',
        '4097',
        get_async_session
    )
    objects_db = await traffic_lights_objects.get_multi(get_async_session)
    exist_obj = await check_light_object_exist('4098888', get_async_session)
    print(obj_db.ext_id)
    print(objects_db)
