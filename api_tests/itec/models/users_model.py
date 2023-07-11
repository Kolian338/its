from typing import Optional
from pydantic import BaseModel, Field, Extra, ValidationError, validator
import allure
from uuid import UUID, uuid4


@allure.step('Создаем модель для запроса (addUser)')
class AddUserRequestModel(BaseModel):
    class Config:
        extra = Extra.forbid

    command: str = "addUser"
    id: Optional[str]
    auth_token: UUID = Field('C31A4C3A-6580-41A4-A013-C263CE9D0A07')
    auth_user: Optional[UUID]
    device: Optional[list[str]]
    user: UUID = Field(default_factory=uuid4)
    isAdmin: Optional[bool]


@allure.title('Создаем модель для ответа addUser')
class AddUserResponseModel(BaseModel):
    class Config:
        extra = Extra.forbid

    command: str = "addUser"
    id: Optional[str]
    status: bool = True


@allure.step('Создаем модель для запроса (deleteUser)')
class DeleteUserRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    command: str = "deleteUser"
    auth_token: UUID = Field('C31A4C3A-6580-41A4-A013-C263CE9D0A07')
    auth_user: Optional[UUID]
    user: UUID


@allure.step('Создаем модель для ответа (deleteUser)')
class DeleteUserResponse(BaseModel):
    class Config:
        extra = Extra.forbid

    command: str = "deleteUser"
    status: bool = True
