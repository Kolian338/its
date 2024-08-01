from pydantic import (
    Field
)

from api_tests.tla.schemas.common import CommonResponse
from api_tests.tla.schemas.common import MyBaseModel


class PartBase(MyBaseModel):
    ofs: int
    offset: int
    guid: str


class PartFull(PartBase):
    gs_caption: str


class GreenRouteBase(MyBaseModel):
    parts: list[PartBase]
    guid: str
    caption: str


class GreenRouteFull(GreenRouteBase):
    parts: list[PartFull]


class ObjBase(MyBaseModel):
    id: int


class ObjFull(ObjBase):
    cmd: int
    command: int


class GreenPartBase(MyBaseModel):
    len: int
    duration: int
    objs: list[ObjBase]
    guid: str
    caption: str


class GreenPartFull(GreenPartBase):
    objs: list[ObjFull]


class InfoFull(MyBaseModel):
    green_route: list[GreenRouteFull] = Field(..., alias='GreenRoute')
    green_part: list[GreenPartFull] = Field(..., alias='GreenPart')


class InfoAll(MyBaseModel):
    green_route: list[GreenRouteBase] = Field(..., alias='GreenRoute')
    green_part: list[GreenPartBase] = Field(..., alias='GreenPart')


class GreenStreetFullResponse(CommonResponse):
    info: list[InfoFull] = Field(..., min_length=1)


class GreenStreetAllResponse(CommonResponse):
    info: list[InfoAll] = Field(..., min_length=1)
