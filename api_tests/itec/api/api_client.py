import allure
from api_tests.common.base_client import ApiClient
from settings import itec_settings


@allure.step('Создаем базового клиента api')
def client_api():
    develop = itec_settings.itec_url
    return ApiClient(base_address=develop)
