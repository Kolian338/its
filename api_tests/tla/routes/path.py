from enum import Enum


class APIPath(str, Enum):
    """
    Константы Path параметров в URL.
    """

    LIGHTS = '/lights'
    DISP_SCHEDULE = '/dispshedule'

    def __str__(self) -> str:
        return self.value
