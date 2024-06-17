from typing import Optional, List, Any
from pydantic import BaseModel, Field, Extra, conint
import allure
from uuid import UUID


@allure.step('Создаем модель для запроса (getDevice)')
class GetDeviceRequestModel(BaseModel):
    command: str = "getDevice"
    auth_token: UUID = Field('C31A4C3A-6580-41A4-A013-C263CE9D0A07')
    auth_user: Optional[UUID] = Field(
        None
    )
    user: UUID


@allure.step('Создаем модель для запроса (getActiveDevice)')
class GetActiveDeviceRequestModel(BaseModel):
    command: str = "getActiveDevice"
    auth_token: UUID = Field('C31A4C3A-6580-41A4-A013-C263CE9D0A07')
    auth_user: Optional[UUID] = Field(
        None
    )


class Result(BaseModel):
    devices: List[str] = None


@allure.step('Создаем модель для ответа (getActiveDevice)')
class GetActiveDeviceResponseModel(BaseModel):
    command: str = "getActiveDevice"
    result: Result = None
    status: bool = True


@allure.step('Создаем модель для ответа (getDevice)')
class GetDeviceResponseModel(BaseModel):
    command: str = 'getDevice'
    result: Result = None
    status: bool = True
