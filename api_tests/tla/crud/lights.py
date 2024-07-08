from sqlalchemy import select

from api_tests.tla.models.lights import TrafficLightsObjects
from core.db import AsyncSessionPg


async def get_obj_by_extid(
        ext_id: str,
        session: AsyncSessionPg
) -> TrafficLightsObjects | None:
    """Возвращает объект TrafficLightsObjects по ext_id"""
    result = await session.execute(
        select(
            TrafficLightsObjects
        ).where(
            TrafficLightsObjects.ext_id == ext_id
        )
    )
    obj_ext_id = result.scalars().first()
    return obj_ext_id
