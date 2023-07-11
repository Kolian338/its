import allure
import json
import pytest
from api_tests.itec.api.api_client import client_api
from api_tests.itec.api.users_api import add_user_api, delete_user_api
from api_tests.itec.models.devices_model import GetActiveDeviceRequestModel
from api_tests.itec.models.users_model import DeleteUserRequest


@pytest.fixture()
@allure.title('Вызываем фикстуру для создания api клиента')
def client():
    return client_api()


@pytest.fixture()
@allure.title('Вызываем фикстуру для создания юзера в api')
@allure.description('Создается юзер в api, после завершения теста удаляется')
def add_user(client, request):
    # Взять модель переданную в фикстуру из теста
    add_user_model = request.param
    # Выполнить запрос к api на создание пользователя
    response = add_user_api(payload=add_user_model, client=client)
    # Возвращаем ответ
    yield {"response": response, "model": add_user_model}
    # Удалить юзера
    user_delete_model = DeleteUserRequest(user=add_user_model.user)
    delete_user_api(payload=user_delete_model, client=client)


@pytest.fixture()
@allure.title('Получаем одно активное устройство')
def get_active_device(client, request):
    count_devices = request.param

    payload = GetActiveDeviceRequestModel()
    payload_json = json.loads(payload.json())

    response = client.post(json=payload_json)
    return response.json()['result']['devices'][0:count_devices]
