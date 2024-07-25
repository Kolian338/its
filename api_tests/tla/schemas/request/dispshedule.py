from datetime import datetime as dt
from enum import StrEnum
from faker import Faker

from pydantic import (
    BaseModel, Field, ConfigDict, field_validator, UUID4,
)
from uuid import uuid4
from api_tests.tla.routes.query import APIQuery

fake = Faker()


class Obj(BaseModel):
    id: str = Field('4097')
    guid: str = Field(default_factory=fake.uuid4)
    command: str = Field('64')


class DispShedule(BaseModel):
    guid: str = Field(default_factory=fake.uuid4)
    caption: str = Field(default_factory=lambda:f'Тестовое расписание. AUTO:{dt.now()}')
    type: str = Field(default_factory=lambda: fake.random_int(0, 6))
    timeon: float = Field(default_factory=fake.unix_time)
    timeoff: float = Field(default_factory=fake.unix_time)
    objs: list[Obj] = Field(default_factory=lambda: [Obj()])
    tasks: list[str] = Field(default_factory=lambda: [fake.uuid4()])


class DispSheduleRequest(BaseModel):
    msource: str = Field(APIQuery.BACKMEGAPOLISURL)
    set_disp_shedule: list[DispShedule] = Field(
        default_factory=lambda: [DispShedule()], alias='SetDispShedule'
    )
