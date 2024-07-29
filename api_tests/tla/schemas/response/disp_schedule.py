from pydantic import BaseModel, Field, ConfigDict

from api_tests.tla.schemas.response.common import CommonResponse


class ObjBase(BaseModel):
    id: int

    model_config = ConfigDict(extra='forbid')


class ObjFull(ObjBase):
    cmd: int
    command: int


class DispSheduleBase(BaseModel):
    active: bool
    timeoff: int
    db_rec_set: int = Field(..., alias='dbRecSet')
    timeon: int
    tasks: list
    time_on: str = Field(..., alias='TimeOn')
    type: int
    guid: str
    time_off: str = Field(..., alias='TimeOff')
    db_cmd_set: int = Field(..., alias='dbCmdSet')
    caption: str
    type_name: str = Field(..., alias='typeName')

    model_config = ConfigDict(extra='forbid')


class DispSheduleAll(DispSheduleBase):
    objs: list[ObjBase]


class DispSheduleFull(DispSheduleBase):
    objs: list[ObjFull]


class DispSheduleBase(CommonResponse):
    model_config = ConfigDict(extra='forbid')


class DispSheduleAllResponse(DispSheduleBase):
    info: list[DispSheduleAll] = Field(..., min_length=1)


class DispSheduleFullResponse(DispSheduleBase):
    info: list[DispSheduleFull] = Field(..., min_length=1)
