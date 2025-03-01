from pydantic import (
    BaseModel, ConfigDict
)


class MyBaseModel(BaseModel):
    """Кастомный базовый класс Pydantic."""
    model_config = ConfigDict(extra='allow')


class CommonResponse(MyBaseModel):
    """Общая схема для ответов."""
    code: str
    amount: int
