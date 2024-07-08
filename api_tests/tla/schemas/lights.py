from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field, ConfigDict


class TdkName(StrEnum):
    MEGAPOLIS = 'Мегаполис/УК-4.1'
    COMKON = 'Комкон'
    AUTHOMATIC = 'Автоматика Д'
    COMSIGNAL = 'Комсигнал'


class Common(BaseModel):
    model_config = ConfigDict(extra='forbid')


class Light(Common):
    priority: int
    tdk: int
    regions: int
    time_utc: int
    time_str: str
    time_rcv: int
    ltakt: int
    lflags: int
    offset: int
    extmode: int
    time_lt: str
    result: str
    lstate: int
    lcycle: int
    source: int
    flags: int
    id: int
    executed: bool
    command: int
    lphase: int
    state: int
    lsource: int
    adp_flags: int = Field(..., alias='adpFlags')
    extsource: int
    time: float
    cycle: int
    mode: int
    lsec: int
    last: int
    code: int
    cmd_ast: int
    tdk_name: str
    time_rcv_its: str
    source_name: str
    command_name: str
    state_name: str
    mode_name: str


class LightStateResponse(Common):
    code: str
    amount: int
    info: list[Light]
