from http import HTTPStatus
from http.client import HTTPException

from api_tests.tla.crud.lights import traffic_lights_objects_crud
from api_tests.tla.models.light_objects import TrafficLightsObjects
from core.db import AsyncSessionPg


async def check_light_object_exist(
        light_object_extid: str,
        session: AsyncSessionPg,
) -> TrafficLightsObjects:
    """Проверка существующего объекта СО по ext_id в БД."""
    light_object = await traffic_lights_objects_crud.get_by_attribute(
        attr_name='ext_id',
        attr_value=light_object_extid,
        session=session
    )
    if light_object is None:
        raise HTTPException(
            HTTPStatus.NOT_FOUND,
        )
    return light_object
