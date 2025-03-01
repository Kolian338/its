from datetime import datetime as dt
from enum import StrEnum

from pydantic import (
    Field, ConfigDict, field_validator, UUID4,
)

from api_tests.tla.schemas.common import CommonResponse, MyBaseModel


def validate_data_format_from_str(value: str, field):
    """Проверка формата даты для схемы для строковых значений."""
    date_formats = {
        'time_rcv_its': '%d.%m.%Y %H:%M:%S',
        'time_lt': '%Y-%m-%dT%H:%M:%S',
        'time_str': '%Y-%m-%dT%H:%M:%SZ',
    }
    date_format = date_formats.get(field.field_name)

    if not dt.strptime(value, date_format):
        raise ValueError(f'Неверный формат даты, ожидается {date_format}')
    return value


def validate_data_format_from_int(value: int):
    """Проверка формата даты для схемы для числовых значений."""
    if not dt.utcfromtimestamp(value):
        raise ValueError('Неверный формат даты, ожидается timestamp')
    return value


class TdkName(StrEnum):
    MEGAPOLIS = 'Мегаполис/УК-4.1'
    COMKON = 'Комкон'
    AUTHOMATIC = 'Автоматика Д'
    COMSIGNAL = 'Комсигнал'
    NOT_DEFINED = 'Не определено'


class Ext(MyBaseModel):
    time_rcv: int | None
    packed: int | None
    body: str | None

    model_config = ConfigDict(extra='forbid')


class LightObject(MyBaseModel):
    """Схема для объекта СО."""
    id: int
    priority: int = Field(None, )
    executed: bool = Field(None, )
    tdk: int
    cmd_guid: UUID4 = Field(None, )
    regions: int = Field(None, )
    ext: Ext = Field(None, )
    time_rcv: int
    lflags: int = Field(None, )
    offset: int
    extmode: int
    lstate: int
    lcycle: int
    ltakt: int = Field(None, )
    source: int
    command: int
    mode: int
    last: int
    code: int = Field(None, )
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
    result: str = Field(None, )
    time: float = Field(None, )
    time_lt: str = Field(None, )
    time_str: str = Field(None, )
    time_utc: int = Field(None, )

    _validate_data_str = field_validator(
        'time_rcv_its', 'time_lt', 'time_str',
    )(validate_data_format_from_str)

    _validate_data_int = field_validator(
        'time_utc',
    )(validate_data_format_from_int)

    model_config = ConfigDict(extra='forbid')


class LightsObjects(LightObject):
    mag: int
    longitude: float
    latitude: float
    way: int | None


class LightStateResponse(CommonResponse):
    """
    Схема ответа по запросу:
    curl --location 'http://traffic-lights-api-develop.k8.sccloud.ru/lights?
    id=4098&state=null&msource=backMegapolisUrl2'
    """
    info: list[LightObject] = Field(..., min_length=1)


class SignalProgram(MyBaseModel):
    """Схема для сигнальной программы."""
    num: int | None = Field(None, )
    com: int = Field(None, )
    ast: int = Field(None, )
    cmd_guid: str = Field(None, )
    result: str = Field(None, )
    source: int = Field(None, )
    ig: list[int] = Field(None, )
    id: int
    bcycle: int = Field(None, )
    state: int = Field(None, )
    cycle: int = Field(None, )
    mode: int = Field(None, )
    lens: list[int] = Field(None, )
    code: int = Field(None, )
    bast: int = Field(None, )
    blens: list[int] = Field(None, )
    phases: list[int] = Field(None, )
    source_name: str = Field(None, )
    state_name: str = Field(None, )
    mode_name: str = Field(None, )

    model_config = ConfigDict(extra='forbid')


class SignalProgramResponse(CommonResponse):
    info: list[SignalProgram] = Field(..., min_length=1)
