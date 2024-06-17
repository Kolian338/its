import allure
from api_tests.common.base_client import ApiClient
from settings import base_settings


@allure.step('Создаем базового клиента api')
def client_api():
    develop = base_settings.itec_url
    chita = "http://192.168.32.55:3000"
    return ApiClient(base_address=develop)
