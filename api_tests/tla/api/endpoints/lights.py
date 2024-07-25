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
        self.base_params: dict = {
            APIQuery.MSOURCE: APIQuery.BACKMEGAPOLISURL,
        }

    def _get_light(self, params: dict) -> Response:
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

    def _get_updated_params(
            self, additional_params: dict[str, int | str]
    ) -> dict[str, int | str]:
        """Добавляет новые параметры к базовым."""
        new_params = self.base_params.copy()
        new_params.update(additional_params)
        return new_params

    @allure.step('Получение состояния СО по id')
    def get_lights_state_by_id(self, id: int | list[int]) -> Response:
        """
        Получение состояния одного или списка СО.

        Возвращает:
            https://gitlab.sccloud.ru/dis/traffic-lights-api/-/blob/develop
            /readme/example_2.md
        """
        additional_params = {
            APIQuery.ID: id,
            APIQuery.STATE: None
        }

        new_params = self._get_updated_params(additional_params)
        return self._get_light(params=new_params)

    @allure.step('Получение списка состояний СО по ids.')
    def get_lights_state_by_ids(self) -> Response:
        """Получение полного списка состояния светофорных объектов."""
        additional_params = {
            APIQuery.IDS: APIQuery.STATE,
        }
        new_params = self._get_updated_params(additional_params)
        return self._get_light(params=new_params)

    @allure.step('Получение текущей сигнальной программы СО.')
    def get_current_signal_program_by_id(
            self, id: int | list[int]
    ) -> Response:
        """Получение текущей сигнальной программы СО."""
        additional_params = {
            APIQuery.ID: id,
            APIQuery.AST: None,
        }

        new_params = self._get_updated_params(additional_params)
        return self._get_light(params=new_params)

    @allure.step('Получение полного списка текущих сигнальных программ СО.')
    def get_current_signal_program_by_ids(self) -> Response:
        """Получение полного списка текущих сигнальных программ СО."""
        additional_params = {
            APIQuery.IDS: APIQuery.ALL,
            APIQuery.AST: None,
        }

        new_params = self._get_updated_params(additional_params)
        return self._get_light(params=new_params)
