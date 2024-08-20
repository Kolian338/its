from pydantic import (
    Field, ConfigDict, field_validator,
)

from api_tests.tla.api.validators.disp_schedule import (
    region_must_be_between_1_and_32)
from api_tests.tla.schemas.common import CommonResponse, MyBaseModel


class ObjBase(MyBaseModel):
    id: int

    model_config = ConfigDict(extra='forbid')


class ObjFull(ObjBase):
    cmd: int
    command: int


class ObjCreateUpdate(ObjBase):
    command: int
    result: str = Field(None, )
    code: int = Field(None, )
    guid: str = Field(None, )


class Tasks(MyBaseModel):
    result: str = Field(None, )
    code: int = Field(None, )
    guid: str = Field(None, )


class DispSheduleBase(MyBaseModel):
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


class DispSheduleCreateUpdate(MyBaseModel):
    time_off: str = Field(..., alias='TimeOff')
    timeoff: str
    result: str
    timeon: str
    type: int
    objs: list[ObjCreateUpdate]
    guid: str
    code: int
    caption: str
    type_name: str = Field(..., alias='typeName')
    id: str = Field(None, )
    region: int
    day_of_week: int = Field(None, alias='DayOfWeek')
    db_rec_set: int = Field(None, alias='dbRecSet')
    db_cmd_set: int = Field(None, alias='dbCmdSet')
    tasks: list[Tasks] = Field(None, )
    time_on: str = Field(None, alias='TimeOn')

    @field_validator('result', mode='after')
    def validate_result(cls, value):
        if value != 'created':
            raise ValueError("Значение должно быть = 'created'")
        return value

    @field_validator('code', mode='after')
    def validate_code(cls, value):
        if value != 201:
            raise ValueError("Коде должен быть = 201")
        return value

    _validate_region = field_validator(
        'region'
    )(region_must_be_between_1_and_32)


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


class DispSheduleCreateUpdateResponse(DispSheduleBase):
    info: list[DispSheduleCreateUpdate] = Field(..., min_length=1)

    def get_guids(self) -> list[str]:
        """
        Возвращает список GUID из всех объектов
        DispSheduleCreateUpdateResponse.

        Returns:
            List[str]: Список GUID.
        """
        return [disp_shedule.guid for disp_shedule in self.info]
