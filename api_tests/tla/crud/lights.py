from sqlalchemy import select

from api_tests.tla.models.traffic_lights_objects import TrafficLightsObjects
from core.db import AsyncSessionPg


async def get_obj_by_extid(
        ext_id: str,
        session: AsyncSessionPg
) -> TrafficLightsObjects | None:
    """
    Запрашивает в БД светофорный объект по ext_id.

    Аргументы:
    session: Асинхронная сессия.

    Возвращает: Объект TrafficLightsObjects.
    """
    result = await session.execute(
        select(
            TrafficLightsObjects
        ).where(
            TrafficLightsObjects.ext_id == ext_id
        )
    )
    obj_ext_id = result.scalars().first()
    return obj_ext_id


async def read_all_objects_from_db(
        session: AsyncSessionPg
) -> list[TrafficLightsObjects]:
    """
    Запрашивает из БД все светофорные объекты.

    Аргументы:
        session: Асинхронная сессия.

    Возвращает: Список объектов TrafficLightsObjects.
    """
    objects = await session.execute(
        select(
            TrafficLightsObjects
        )
    )
    return objects.scalars().all()
