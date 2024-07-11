from enum import Enum

from core.config import tla_settings


class APIQuery(str, Enum):
    """
    Константы Query параметров в URL.
    """

    ID = 'id'
    IDS = 'ids'
    MSOURCE = 'msource'
    EXTENDED = 'extended'
    STATE = 'state'
    BACKMEGAPOLISURL = tla_settings.msource

    def __str__(self) -> str:
        return self.value
