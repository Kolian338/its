from datetime import datetime

from pydantic import (
    BaseModel, ConfigDict, UUID4, Json
)


class ObjBase(BaseModel):
    extId: str
    command: str

    model_config = ConfigDict(extra='forbid')


class DispSheduleDB(BaseModel):
    id: UUID4
    guid: str
    caption: str
    time_on: datetime
    time_off: datetime
    type: str
    type_name: str
    objs: list[ObjBase]
    creation_time: int
    update_time: int
    creation_author: UUID4
    update_author: UUID4
    green_route_ids: Json
    mo_id: UUID4
    source: str
    msource: str

    model_config = ConfigDict(extra='forbid')
