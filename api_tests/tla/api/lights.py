import json
import allure
from api_tests.common.base_client import ApiClient
from settings import tla_settings


@allure.step('Получение списка светофоров')
def get_lights(client: ApiClient):
    response = client.get(
        path='/lights', params=f'ids=full&msource={tla_settings.msource}'
    )
    return response
