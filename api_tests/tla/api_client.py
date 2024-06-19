import allure
from api_tests.common.base_client import ApiClient
from settings import base_settings


@allure.step('Создаем базового клиента api')
def client_api():
    develop = base_settings.tla_url
    return ApiClient(base_address=develop)
