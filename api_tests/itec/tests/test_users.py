import allure
import pytest

from api_tests.itec.api.users_api import add_user_api, delete_user_api
from api_tests.itec.api.devices_api import get_device_api

from api_tests.itec.schemas.user import AddUserRequestModel, \
    AddUserResponseModel, DeleteUserRequest, DeleteUserResponse
from api_tests.itec.schemas.device import GetDeviceRequestModel

from api_tests.itec.assertions.schema import validate_schema
from truth.truth import AssertThat

from api_tests.itec.helper.devices import get_devices_from_response, \
    get_some_active_device


# TODO Продумать как вынести создание и удаление юзера в фикстуру


class TestUsers:
    # Передаем модель в маркер что бы потом использовать его в фикстуре
    @pytest.mark.parametrize('add_user',
                             [AddUserRequestModel(id='1')],
                             indirect=True
                             )
    @allure.title('Создается пользователь без устройств')
    def test_add_user_new_user_user_added(self, add_user):
        response = add_user.get('response')
        json_response = response.json()

        AssertThat(response.status_code).IsEqualTo(200)
        validate_schema(json_response, AddUserResponseModel().schema())

    @allure.title(
        'Создаем пользователя с одним, несколькими, пустым списком устройств')
    @pytest.mark.parametrize('add_user',
                             [
                                 AddUserRequestModel(
                                     device=get_some_active_device(
                                         count_devices=0)),
                                 AddUserRequestModel(
                                     device=get_some_active_device(
                                         count_devices=1)),
                                 AddUserRequestModel(
                                     device=get_some_active_device(
                                         count_devices=2))
                             ],
                             ids=[
                                 'add_user_without_devices',
                                 'add_user_with_one_device',
                                 'add_user_with_two_devices'
                             ],
                             indirect=True
                             )
    def test_add_user_add_devices_to_user_user_with_devices_exist(self,
                                                                  add_user,
                                                                  client):
        # Получаем структуру ответа
        add_user_response = add_user.get('response')

        # Проверка структуры ответа от api по созданию пользователя
        AssertThat(add_user_response.status_code).IsEqualTo(200)
        validate_schema(add_user_response.json(),
                        AddUserResponseModel().schema())

        # Получить модель юзера
        add_user_model = add_user.get('model')
        # Получить модель устройств юзера
        get_device_model = GetDeviceRequestModel(user=add_user_model.user)

        # Запрашиваем устройства юзера
        get_device_response = get_device_api(
            payload=get_device_model,
            client=client
        )
        # Получить множество устройств юзера от api
        devices_response = get_devices_from_response(
            get_device_response.json())
        set_devices_from_response = set(devices_response)
        # Получить множество устройств юзера из переданной модели
        set_user_devices_from_model = set(add_user_model.device)

        # Проверить что устройства добавились пользователю
        AssertThat(set_devices_from_response).ContainsExactlyElementsIn(
            set_user_devices_from_model)

    @allure.title('Удаляется только что созданный пользователь')
    def test_delete_user_new_user_user_deleted(self, client):
        user_add_model = AddUserRequestModel()
        user_delete_model = DeleteUserRequest(user=user_add_model.user)
        add_user_api(payload=user_add_model, client=client)

        response = delete_user_api(payload=user_delete_model, client=client)
        json_response = response.json()

        AssertThat(response.status_code).IsEqualTo(200)
        validate_schema(json_response, DeleteUserResponse().schema())
