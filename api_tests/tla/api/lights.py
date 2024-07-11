import allure
from requests import Response

from api_tests.common.base_client import ApiClient
from api_tests.tla.routes.path import APIPath
from api_tests.tla.routes.query import APIQuery


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

    def _get_light(self, params) -> Response:
        """
        Общий метод для получения состояния светофорного объекта.

        Параметры:
            params: str
                Параметры запроса
        Возвращает:
            Объект Response
        """
        params_string = "&".join(
            [f"{key}={value}" if value is not None else key for key, value in
             params.items()]
        )
        return self.client.get(
            path=self.path,
            params=params_string
        )

    @allure.step('Получение состояния СО по id')
    def get_lights_state_by_id(self, id: int | list[int]) -> Response:
        """
        Получение состояния одного или списка СО.

        Возвращает:
            https://gitlab.sccloud.ru/dis/traffic-lights-api/-/blob/develop
            /readme/example_2.md
        """
        params = {
            APIQuery.ID: id,
            APIQuery.MSOURCE: APIQuery.BACKMEGAPOLISURL,
            APIQuery.STATE: None
        }

        return self._get_light(params=params)

    @allure.step('Получение состояния СО')
    def get_lights_state_by_ids(self) -> Response:
        """Получение полного списка состояния светофорных объектов."""
        params = {
            APIQuery.IDS: APIQuery.STATE,
            APIQuery.MSOURCE: APIQuery.BACKMEGAPOLISURL,
        }

        return self._get_light(params=params)
