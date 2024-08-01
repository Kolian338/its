from datetime import datetime as dt

from faker import Faker
from pydantic import (
    Field, ConfigDict, )

from api_tests.tla.routes.query import APIQuery
from api_tests.tla.schemas.common import MyBaseModel

fake = Faker()


class Obj(MyBaseModel):
    id: str = Field('4097')
    guid: str = Field(default_factory=fake.uuid4)
    command: str = Field('64')

    model_config = ConfigDict(extra='forbid')


class DispShedule(MyBaseModel):
    guid: str = Field(default_factory=fake.uuid4)
    caption: str = Field(
        default_factory=lambda: f'Тестовое расписание. AUTO:{dt.now()}')
    type: str = Field(default_factory=lambda: fake.random_int(0, 6))
    timeon: float = Field(default_factory=fake.unix_time)
    timeoff: float = Field(default_factory=fake.unix_time)
    objs: list[Obj] = Field(default_factory=lambda: [Obj()])
    tasks: list[str] = Field(default_factory=lambda: [fake.uuid4()])

    model_config = ConfigDict(extra='forbid')


class DispSheduleRequest(MyBaseModel):
    msource: str = Field(APIQuery.BACKMEGAPOLISURL)
    set_disp_shedule: list[DispShedule] = Field(
        default_factory=lambda: [DispShedule()], alias='SetDispShedule'
    )

    model_config = ConfigDict(extra='forbid')

    def get_guids(self) -> list[str]:
        """
        Возвращает список GUID из всех объектов DispSheduleRequest.

        Returns:
            List[str]: Список GUID.
        """
        return [disp_shedule.guid for disp_shedule in self.set_disp_shedule]
