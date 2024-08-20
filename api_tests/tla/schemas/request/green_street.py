from datetime import datetime as dt
from api_tests.tla.constants import Body

from faker import Faker
from pydantic import (
    Field
)

from api_tests.tla.constants import Body
from api_tests.tla.routes.query import APIQuery
from api_tests.tla.schemas.common import MyBaseModel

fake = Faker()


class Obj(MyBaseModel):
    id: str = Field('4097')
    com: str = Field('64')


class Part(MyBaseModel):
    """Участок."""
    guid: str = Field(default_factory=fake.uuid4)
    ofs: int = Field(default=Body.OFS)


class AddGreenPartItem(MyBaseModel):
    """Элемент участка."""
    region: int = Field(default=Body.REGION)
    guid: str = Field(default_factory=fake.uuid4)
    caption: str = Field(
        default_factory=lambda: f'Тестовый участок. AUTO:{dt.now()}')
    len: int = Field(default=120)
    objs: list[Obj] = Field(default_factory=lambda: [Obj()])


class AddGreenRoutItem(MyBaseModel):
    """Маршрут."""
    caption: str = Field(
        default_factory=lambda: f'Тестовый маршрут. AUTO:{dt.now()}')
    region: int = Field(default=Body.REGION)
    guid: str = Field(default_factory=fake.uuid4)
    parts: list[Part] = Field(default_factory=lambda: [Part()])


class AddGreenPartRequest(MyBaseModel):
    """Объект для добавления участков зеленых улиц."""
    msource: str = Field(APIQuery.BACKMEGAPOLISURL)
    add_green_part: list[AddGreenPartItem] = Field(
        default_factory=lambda: [AddGreenPartItem()], alias='AddGreenPart'
    )


class AddGreenRouteRequest(MyBaseModel):
    """Объект для добавления маршрутов зеленых улиц."""
    msource: str = Field(APIQuery.BACKMEGAPOLISURL)
    add_green_rout: list[AddGreenRoutItem] = Field(
        default_factory=lambda: [AddGreenRoutItem()], alias='AddGreenRout'
    )
