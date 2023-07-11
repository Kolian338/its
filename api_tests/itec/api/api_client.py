import requests
import allure


class ApiClientItec:
    def __init__(self, base_address):
        self.base_address = base_address

    @allure.step('Отправляем post запрос на {path}')
    def post(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        return requests.get(url=url, params=params, headers=headers)


@allure.step('Создаем базового клиента api')
def client_api():
    develop = "http://192.168.32.67:3000"
    chita = "http://192.168.32.55:3000"
    return ApiClientItec(base_address=develop)
