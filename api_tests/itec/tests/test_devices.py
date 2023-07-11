import allure
import pytest

from truth.truth import AssertThat
from api_tests.itec.assertions.schema import validate_schema

from api_tests.itec.api.devices_api import \
    get_active_device_api, get_device_api

from api_tests.itec.models.devices_model import \
    GetActiveDeviceRequestModel, GetActiveDeviceResponseModel, \
    GetDeviceRequestModel, GetDeviceResponseModel
from api_tests.itec.models.users_model import \
    AddUserRequestModel

from api_tests.itec.helper.devices import get_devices_from_response, \
    get_some_active_device


class TestDevices:
    @allure.title('Можно получить список всех активных устройств')
    def test_get_active_device_devices_exist(self, client):
        active_device_model = GetActiveDeviceRequestModel()

        response = get_active_device_api(payload=active_device_model, client=client)
        json_response = response.json()

        AssertThat(response.status_code).IsEqualTo(200)
        validate_schema(json_response, GetActiveDeviceResponseModel().schema())

    @allure.title('Можно получить добавленные устройства у пользователя')
    @pytest.mark.parametrize('add_user',
                             [
                                 AddUserRequestModel(device=get_some_active_device(count_devices=0)),
                                 AddUserRequestModel(device=get_some_active_device(count_devices=1)),
                                 AddUserRequestModel(device=get_some_active_device(count_devices=2))
                             ],
                             ids=[
                                 'add_user_without_devices',
                                 'add_user_with_one_device',
                                 'add_user_with_two_devices'
                             ],
                             indirect=True
                             )
    def test_get_device_add_devices_added_devices_exist(self, add_user, client):
        # Получить модель юзера
        add_user_model = add_user.get('model')
        # Получить модель устройств юзера
        get_device_model = GetDeviceRequestModel(user=add_user_model.user)

        # Запрашиваем устройства юзера
        get_device_response = get_device_api(payload=get_device_model, client=client)
        get_device_response_json = get_device_response.json()

        # Получить множество устройств юзера от api
        devices_response = get_devices_from_response(get_device_response_json)
        set_devices_from_response = set(devices_response)
        # Получить множество устройств юзера из переданной модели
        set_user_devices_from_model = set(add_user_model.device)

        # Проверки
        AssertThat(get_device_response.status_code).IsEqualTo(200)
        validate_schema(get_device_response_json, GetDeviceResponseModel().schema())
        AssertThat(set_devices_from_response).ContainsExactlyElementsIn(set_user_devices_from_model)
