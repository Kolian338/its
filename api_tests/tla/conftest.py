import allure
import pytest
from api_tests.tla.api.api_client import client_api


@pytest.fixture()
@allure.title('Вызываем фикстуру для создания api клиента')
def client():
    return client_api()
