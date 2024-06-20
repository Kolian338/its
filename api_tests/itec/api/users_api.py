import json
import allure
from api_tests.itec.schemas.user import \
    AddUserRequestModel, DeleteUserRequest


@allure.step('Создаем пользователя в api')
def add_user_api(payload: AddUserRequestModel, client):
    payload_json = json.loads(payload.json())

    response = client.post(json=payload_json)
    return response


def update_user_api():
    pass


@allure.step('Удаляем пользователя из api')
def delete_user_api(payload: DeleteUserRequest, client):
    payload_json = json.loads(payload.json())

    response = client.post(json=payload_json)
    return response
