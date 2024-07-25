from requests import Response

from api_tests.common.base_client import ApiClient
from api_tests.tla.routes.path import APIPath
from api_tests.tla.schemas.request.dispshedule import DispSheduleRequest


class DispScheduleClient:
    """
    Класс являющийся клиентом для запросов к эндпоинту /dispshedule API.
    """

    def __init__(self, client: ApiClient):
        """
        Инициализация клиента для работы с API диспетчерского расписания.

        :param client: Экземпляр клиента API.
        """
        self.client: ApiClient = client
        self.path: APIPath = APIPath.DISP_SCHEDULE

    def create_disp_shedule(self, payload: DispSheduleRequest) -> Response:
        """
        Создание диспетчерского расписания с помощью API.

        :param payload: Данные запроса в формате модели DispSheduleRequest.
        :return: Ответ от сервера.
        """
        payload = payload.model_dump(by_alias=True)
        return self.client.post(
            self.path, json=payload
        )
