from pydantic import (
    BaseModel, Field, ConfigDict, field_validator, model_validator
)

from api_tests.tla.schemas.common import CommonResponse


class ObjBase(BaseModel):
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


class DispSheduleCreateUpdate(BaseModel):
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
