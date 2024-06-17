from typing import Optional
from pydantic import BaseModel, Field, Extra, ValidationError, validator
import allure
from uuid import UUID, uuid4


@allure.step('Создаем модель для запроса (addUser)')
class AddUserRequestModel(BaseModel):
    command: str = "addUser"
    id: Optional[str] = Field(
        None
    )
    auth_token: UUID = Field('C31A4C3A-6580-41A4-A013-C263CE9D0A07')
    auth_user: Optional[UUID] = Field(
        None
    )
    device: Optional[list[str]] = Field(
        None
    )
    user: UUID = Field(default_factory=uuid4)
    isAdmin: Optional[bool] = Field(
        None
    )


@allure.title('Создаем модель для ответа addUser')
class AddUserResponseModel(BaseModel):
    command: str = 'addUser'
    id: Optional[str] = Field(
        None
    )
    status: bool = True


@allure.step('Создаем модель для запроса (deleteUser)')
class DeleteUserRequest(BaseModel):
    command: str = "deleteUser"
    auth_token: UUID = Field('C31A4C3A-6580-41A4-A013-C263CE9D0A07')
    auth_user: Optional[UUID] = Field(
        None
    )
    user: UUID


@allure.step('Создаем модель для ответа (deleteUser)')
class DeleteUserResponse(BaseModel):
    command: str = "deleteUser"
    status: bool = True
