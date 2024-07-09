import allure
import pytest

from api_tests.tla.api.lights import LightsClient
from api_tests.tla.assertions.schema import validate_schema
from api_tests.tla.crud.lights import (
    get_obj_by_extid, read_all_objects_from_db
)
from api_tests.tla.schemas.lights import LightStateResponse


@allure.title('Получение состояния светофорного объекта.')
def test_get_light_state(lights_client: LightsClient):
    response = lights_client.get_lights_state(ids=4097)
    print(response.json())

    assert response.status_code == 200
    validate_schema(
        response.json(), LightStateResponse.model_json_schema()
    )


# Для тестов к БД
@pytest.mark.asyncio
async def test_async_function(get_async_session):
    obj = await get_obj_by_extid('4097', get_async_session)
    objects = await read_all_objects_from_db(get_async_session)
    print(objects[0].tdk_name)
