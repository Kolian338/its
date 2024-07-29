from requests import Response

from api_tests.tla.api.endpoints.base import ClientBase
from api_tests.tla.routes.query import APIQuery
from api_tests.tla.schemas.request.dispshedule import DispSheduleRequest


class DispScheduleClient(ClientBase):
    """
    Класс являющийся клиентом для запросов к эндпоинту /dispshedule API.
    """

    def get_disp_shedule(
            self, ids: str
    ) -> Response:
        """
         Получает диспетчерское расписание на основе заданных параметров.

         Параметры:
         ----------
         ids : str
             Идентификаторы расписаний. Может быть 'full' или 'all'.

         Возвращает:
         -----------
         Response
             Объект ответа, содержащий данные диспетчерского расписания.

         Исключения:
         -----------
         ValueError
             Если передан недопустимый параметр ids.
         """
        if ids == APIQuery.FULL:
            additional_params = {
                APIQuery.IDS: APIQuery.FULL,
            }
        elif ids == APIQuery.ALL:
            additional_params = {
                APIQuery.IDS: APIQuery.ALL,
            }
        else:
            raise ValueError('Нет такого параметра')

        new_params = self.get_updated_params(additional_params)
        return self.get(new_params)

    def create_disp_shedule(
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
