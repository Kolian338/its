import allure
from api_tests.common.base_client import ApiClient
from core.config import itec_settings


@allure.step('Создаем базового клиента api')
def client_api():
    develop = itec_settings.url
    return ApiClient(base_address=develop)
