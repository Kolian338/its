from pydantic import (
    BaseModel,
)


class CommonResponse(BaseModel):
    """Общая схема для ответов."""
    code: str
    amount: int
