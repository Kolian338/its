from pydantic import (
    Field, field_validator
)

from api_tests.tla.api.validators.green_street import result_must_be_accepted
from api_tests.tla.schemas.common import CommonResponse
from api_tests.tla.schemas.common import MyBaseModel
from api_tests.tla.schemas.mixins.green_street import GuidExtractionMixin


class PartBase(MyBaseModel):
    ofs: int
    offset: int
    guid: str


class PartFull(PartBase):
    gs_caption: str = Field(None, )


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


class GreenStreetAllResponse(CommonResponse, GuidExtractionMixin):
    info: list[InfoAll] = Field(..., min_length=1)


class ObjPart(ObjBase):
    com: int


class Part(MyBaseModel):
    ofs: int
    result: str
    guid: str
    code: int


class InfoItemFromPart(MyBaseModel):
    """Участок."""
    len: int
    result: str
    region: int
    objs: list[ObjPart]
    guid: str
    code: int
    caption: str


class InfoItemFromRout(MyBaseModel):
    """Маршрут с участком."""
    parts: list[Part]
    result: str
    region: int
    guid: str
    code: int
    caption: str


class InfoItemDeleted(MyBaseModel):
    """Удаление участка."""
    result: str
    guid: str
    code: int

    _validate_result = field_validator(
        'result'
    )(result_must_be_accepted)


class GreenPartResponse(CommonResponse, GuidExtractionMixin):
    """Ответ для создания участка (AddGreenPart)."""
    info: list[InfoItemFromPart] = Field(..., min_length=1)


class GreenRoutResponse(CommonResponse, GuidExtractionMixin):
    """Ответ для создания маршрута (AddGreenRout)."""
    info: list[InfoItemFromRout] = Field(..., min_length=1)


class GreenPartOrRouteDeleteResponse(CommonResponse):
    """Ответ для удаления маршрута или участка."""
    info: list[InfoItemDeleted] = Field(..., min_length=1)
