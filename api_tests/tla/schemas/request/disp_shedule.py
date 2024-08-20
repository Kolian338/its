from datetime import datetime as dt

from faker import Faker
from pydantic import (
    Field, ConfigDict, field_validator
)

from api_tests.common.helper.common_helper import (
    current_unix_time, next_hour_unix_time
)
from api_tests.tla.api.validators.disp_schedule import (
    region_must_be_between_1_and_32
)
from api_tests.tla.routes.query import APIQuery
from api_tests.tla.schemas.common import MyBaseModel
from api_tests.tla.constants import Body

fake = Faker()


class Obj(MyBaseModel):
    id: str = Field('4097')
    guid: str = Field(None, )
    command: str = Field('64')


class DispShedule(MyBaseModel):
    guid: str = Field(default_factory=fake.uuid4)
    caption: str = Field(
        default_factory=lambda: f'Тестовое расписание. AUTO:{dt.now()}')
    type: str = Field(default=1)
    timeon: float = Field(default_factory=current_unix_time)
    timeoff: float = Field(default_factory=next_hour_unix_time)
    objs: list[Obj] = Field(default_factory=lambda: [Obj()])
    tasks: list[str] = Field(default_factory=lambda: [fake.uuid4()])
    region: int = Field(default=Body.REGION)

    _validate_region = field_validator(
        'region'
    )(region_must_be_between_1_and_32)


class DispSheduleRequest(MyBaseModel):
    msource: str = Field(APIQuery.BACKMEGAPOLISURL)
    set_disp_shedule: list[DispShedule] = Field(
        default_factory=lambda: [DispShedule()], alias='SetDispShedule'
    )

    def get_guids(self) -> list[str]:
        """
        Возвращает список GUID из всех объектов DispSheduleRequest.

        Returns:
            List[str]: Список GUID.
        """
        return [disp_shedule.guid for disp_shedule in self.set_disp_shedule]
