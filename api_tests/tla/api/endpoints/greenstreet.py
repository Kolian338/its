from requests import Response

from api_tests.tla.api.endpoints.base import ClientBase


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
