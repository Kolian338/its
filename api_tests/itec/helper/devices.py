import allure
import json
from api_tests.itec.schemas.device import GetActiveDeviceRequestModel
from api_tests.itec.api.api_client import client_api


@allure.title('Получаем список устройств юзера')
def get_devices_from_response(json_response: dict):
    return list(json_response.get('result').get('devices'))


# TODO Проверять если нет столько устройств
@allure.title('Получаем одно активное устройство')
def get_some_active_device(count_devices: int):
    payload = GetActiveDeviceRequestModel()
    payload_json = json.loads(payload.json())

    response = client_api().post(json=payload_json)
    return response.json()['result']['devices'][0:count_devices]
