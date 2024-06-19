from pydantic import BaseModel, Field
from typing import Any
from enum import Enum, StrEnum


class TdkName(StrEnum):
    MEGAPOLIS = 'Мегаполис/УК-4.1'
    COMKON = 'Комкон'
    AUTHOMATIC = 'Автоматика Д'
    COMSIGNAL = 'Комсигнал'


class Lights(BaseModel):
    id: int
    tdk: int
    street1: str
    street2: str
    mag: int
    longitude: float
    latitude: float
    time_rcv: int
    flags: int
    state: int
    source: int
    command: int
    offset: int
    mode: int
    last: int
    lcycle: int
    lsec: int
    lphase: int
    lsource: int
    lstate: int
    lflags: int
    adp_flags: int = Field(
        ..., alias='adpFlags'
    )
    way: int
    ext: Any
    tdk_name: TdkName = Field(
        ..., description='Расшифровка значения из поля tdk'
    )
    source_name: str
    command_name: str
    state_name: str
    mode_name: str
    time_rcv_its: str
