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

    @allure.step('Получение состояния светофорных объектов')
    def get_lights_state(
            self, id: int | list[int] = None
    ) -> Response:
        """
        Получение состояния одного или списка светофорных объектов (СО).

        Параметры:
            id: int | list[int] | None
                Идентификатор одного СО или список идентификаторов СО.
                Если None, возвращает полный список состояния светофорных
                 объектов.

        Возвращает:
            Объект Response.
        """
        if id is None:
            additional_params = {
                APIQuery.IDS: APIQuery.STATE,
            }
        else:
            additional_params = {
                APIQuery.ID: id,
                APIQuery.STATE: None,
            }

        new_params = self._get_updated_params(additional_params)
        return self._get_light(params=new_params)

    @allure.step('Получение текущей сигнальной программы СО.')
    def get_signal_program(
            self, id: int | list[int] = None
    ) -> Response:
        """
        Получение текущей сигнальной программы СО или полного списка текущих
         сигнальных программ СО.

        Параметры:
            id: int | list[int] | None
                Идентификатор одного СО или список идентификаторов СО.
                Если None, возвращает полный список текущих
                 сигнальных программ СО.

        Возвращает:
            Объект Response.
        """
        if id is None:
            additional_params = {
                APIQuery.IDS: APIQuery.ALL,
                APIQuery.AST: None,
            }
        else:
            additional_params = {
                APIQuery.ID: id,
                APIQuery.AST: None,
            }

        new_params = self._get_updated_params(additional_params)
        return self._get_light(params=new_params)
