from sqlalchemy import select

from api_tests.tla.crud.base import CRUDBase
from api_tests.tla.models.disp_schedule import TrafficLightsDispShedule
from core.db import AsyncSessionPg


class CRUDDispShedule(CRUDBase):

    async def get_by_guid(
            self,
            guid: str,
            session: AsyncSessionPg,
    ):
        """
        Получает объект диспетчерского расписания по GUID.

        :param guid: GUID для поиска
        :param session: Сессия для выполнения запроса
        :return: Объект диспетчерского расписания или None, если не найден
        """
        db_obj = await session.execute(
            select(self.model).where(
                self.model.guid == guid
            )
        )

        return db_obj.scalars().first()

    async def get_by_guids(
            self,
            guids: list[str],
            session: AsyncSessionPg
    ):
        """
        Получает объекты диспетчерского расписания по нескольким GUID.

        :param guids: Список GUID для поиска
        :param session: Сессия для выполнения запроса
        :return: Список объектов диспетчерского расписания
        """
        result = await session.execute(
            select(
                self.model
            ).where(
                self.model.guid.in_(guids))
        )
        return result.scalars().all()


disp_shedule_crud = CRUDDispShedule(TrafficLightsDispShedule)
