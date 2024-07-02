import allure
from requests import Response

from api_tests.common.base_client import ApiClient
from api_tests.tla.routes.path import APIPath
from api_tests.tla.routes.query import APIQuery
from settings import MsourceEnum, tla_settings


class LightsClient:
    """
    Объект являющийся клиентом для запросов к эндпоинтам API.

    Атрибуты
    --------
    client: ApiClient
        Объект клиента для запросов через requests
    path: APIPath
        Ручка в url
    msource: MsourceEnum
        Переменная по котороый берется адрес для мегаполиса
    """

    def __init__(self, client: ApiClient):
        self.client: ApiClient = client
        self.path: APIPath = APIPath.LIGHTS
        self.msource: MsourceEnum = tla_settings.msource

    @allure.step('Получение расширенного состояния СО')
    def get_light_extend_state(self, id: str) -> Response:
        """
        Получение расширенного состояния только одного светофорного объекта.

        Параметры:
            id: str
                Уникальный номер объекта (id светофора)

        Возвращает:
            https://gitlab.sccloud.ru/dis/traffic-lights-api/-/blob/develop
            /readme/example_3.md
        """
        return self.client.get(
            path=self.path,
            params=(
                f'{APIQuery.ID}={id}'
                f'&{APIQuery.EXTENDED}'
                f'&{APIQuery.MSOURCE}={self.msource}')
        )
