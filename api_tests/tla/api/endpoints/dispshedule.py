from requests import Response

from api_tests.tla.api.endpoints.base import ClientBase
from api_tests.tla.schemas.request.disp_shedule import DispSheduleRequest


class DispScheduleClient(ClientBase):
    """
    Класс являющийся клиентом для запросов к эндпоинту /dispshedule API.
    """

    def get_disp_shedule(
            self, ids: str
    ) -> Response:
        """
        Получение полного(full) или краткого (all) списка дисп.расписаний.
        """
        return self.get_full_or_all_objs(ids)

    async def create_disp_shedule(
            self,
            payload: DispSheduleRequest
    ) -> Response:
        """
        Создание диспетчерского расписания с помощью API.

        :param payload: Данные запроса в формате модели DispSheduleRequest.
        :return: Ответ от сервера.
        """
        payload = payload.model_dump(by_alias=True)
        return self.client.post(
            self.path, json=payload
        )
