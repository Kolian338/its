from requests import Response

from api_tests.tla.api.endpoints.base import ClientBase
from api_tests.tla.schemas.request.green_street import (
    AddGreenPartRequest, AddGreenRouteRequest
)


class GreenStreetClient(ClientBase):
    """
    Класс являющийся клиентом для запросов к эндпоинту /greenstreet API.
    """

    def get_green_street(
            self, ids: str
    ) -> Response:
        """
        Получение полного(full) или краткого (all) списка
         участков и маршрутов зеленых улиц.
        """
        return self.get_full_or_all_objs(ids)

    def create_part(
            self,
            payload: AddGreenPartRequest
    ) -> Response:
        """
        Создание участка зеленой улицы с помощью API.

        :param payload: Данные запроса в формате модели AddGreenPartRequest.
        :return: Ответ от сервера.
        """
        payload = payload.model_dump(by_alias=True)
        return self.client.post(
            self.path, json=payload
        )

    def create_route(
            self,
            payload: AddGreenRouteRequest
    ) -> Response:
        """
        Создание маршрута зеленой улицы с помощью API.

        :param payload: Данные запроса в формате модели AddGreenRouteRequest.
        :return: Ответ от сервера.
        """
        payload = payload.model_dump(by_alias=True)
        return self.client.post(
            self.path, json=payload
        )
