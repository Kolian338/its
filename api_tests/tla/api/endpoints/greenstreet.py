from requests import Response

from api_tests.tla.api.endpoints.base import ClientBase
from api_tests.tla.routes.query import APIQuery
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
        return self.client.post(
            self.path, json=payload.model_dump(by_alias=True)
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

    def delete_part(
            self,
            guid: list[str] | str,
    ) -> Response:
        """
        Удаляет участок зеленой улицы по его уникальному идентификатору (GUID)
        с помощью API.
        """
        return self.delete_obj(guid, APIQuery.DELETE)

    def delete_route(
            self,
            guid: list[str] | str,
    ) -> Response:
        """
        Удаляет маршрут зеленой улицы по его уникальному идентификатору (GUID)
        с помощью API.
        """
        return self.delete_obj(guid, APIQuery.DELETE_ROUTE)

    def delete_obj(
            self, guid: list[str] | str,
            query_type: type(APIQuery)
    ) -> Response:
        """
        Удаляет объект (участок или маршрут) по его уникальному
         идентификатору (GUID).

        :param guid: Один или несколько уникальных идентификаторов (GUID).
        :param query_type: Тип запроса для удаления (DELETE или DELETE_ROUTE).
        :return: Ответ от сервера.

        Примечание:
        guids_string: Преобразует список уникальных идентификаторов (GUID)
        в строку формата массива.
        """
        guids_string = f"[{''.join(guid)}]"
        additional_params = {query_type: guids_string}
        new_params = self.get_updated_params(additional_params)
        return self.client.get(self.path, params=new_params)
