import json
import allure
from api_tests.itec.schemas.device import \
    GetDeviceRequestModel, GetActiveDeviceRequestModel


@allure.step('Запрашиваем устройства пользователя в api (getDevice)')
def get_device_api(payload: GetDeviceRequestModel, client):
    payload_json = json.loads(payload.json())

    response = client.post(json=payload_json)
    return response


@allure.step('Запрашиваем активные устройства в api (getActiveDevice)')
def get_active_device_api(payload: GetActiveDeviceRequestModel, client):
    payload_json = json.loads(payload.json())

    response = client.post(json=payload_json)
    return response
