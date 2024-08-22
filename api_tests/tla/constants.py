from enum import StrEnum, IntEnum, Enum


class RequestBody(IntEnum):
    """
    Константы для тела запроса.
    """

    REGION = 1
    OFS = 60  # смещение/задержка включения участка (секунды > 0)

    def __str__(self) -> int:
        return self.value


class ResponseBody(StrEnum):
    """
    Константы для тела ответа.
    """

    DELETED = 'deleted'

    def __str__(self) -> str:
        return self.value
