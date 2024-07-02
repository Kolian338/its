import allure

from api_tests.common.base_client import ApiClient
from settings import tla_settings


@allure.step('Создаем базового клиента api')
def client_api():
    develop = tla_settings.url
    return ApiClient(base_address=develop)
