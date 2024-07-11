from datetime import datetime as dt
from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict, field_validator


class TdkName(StrEnum):
    MEGAPOLIS = 'Мегаполис/УК-4.1'
    COMKON = 'Комкон'
    AUTHOMATIC = 'Автоматика Д'
    COMSIGNAL = 'Комсигнал'


class Ext(BaseModel):
    time_rcv: int | None
    packed: int | None
    body: str | None

    model_config = ConfigDict(extra='forbid')


class LightObject(BaseModel):
    """Схема для объекта СО."""
    id: int
    tdk: int
    ext: Ext = Field(None,)
    time_rcv: int
    lflags: int = Field(None,)
    offset: int
    extmode: int
    lstate: int
    lcycle: int
    source: int
    command: int
    mode: int
    last: int
    lsec: int
    lphase: int
    lsource: int
    flags: int
    state: int
    adp_flags: int = Field(..., alias='adpFlags')
    tdk_name: TdkName
    source_name: str
    command_name: str
    state_name: str
    mode_name: str
    time_rcv_its: str
    cmd_ast: int
    cycle: int
    extsource: int

    model_config = ConfigDict(extra='forbid')

    @field_validator('time_rcv_its')
    def validate_data_format(cls, value: str):
        if not dt.strptime(value, '%d.%m.%Y %H:%M:%S'):
            raise ValueError('Ошибка даты')
        return value


class LightsObjects(LightObject):
    mag: int
    longitude: float
    latitude: float
    way: int | None


class LightStateResponse(BaseModel):
    """
    Схема ответа по запросу:
    curl --location 'http://traffic-lights-api-develop.k8.sccloud.ru/lights?
    id=4098&state=null&msource=backMegapolisUrl2'
    """
    code: str
    amount: int
    info: list[LightObject] = Field(..., min_length=1)
