import allure
from requests import Response

from api_tests.tla.api.endpoints.base import ClientBase
from api_tests.tla.routes.query import APIQuery


class LightsClient(ClientBase):
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
        if not id:
            additional_params = {
                APIQuery.IDS: APIQuery.STATE,
            }
        else:
            additional_params = {
                APIQuery.ID: id,
                APIQuery.STATE: None,
            }

        new_params = self.get_updated_params(additional_params)
        return self.get(params=new_params)

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
        if not id:
            additional_params = {
                APIQuery.IDS: APIQuery.ALL,
                APIQuery.AST: None,
            }
        else:
            additional_params = {
                APIQuery.ID: id,
                APIQuery.AST: None,
            }

        new_params = self.get_updated_params(additional_params)
        return self.get(params=new_params)
