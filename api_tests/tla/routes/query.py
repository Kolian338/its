from enum import Enum


class APIQuery(str, Enum):
    """
    Константы Query параметров в URL.
    """

    ID = 'id'
    IDS = 'ids'
    MSOURCE = 'msource'
    EXTENDED = 'extended'

    def __str__(self) -> str:
        return self.value
