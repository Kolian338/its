from requests import Response

from api_tests.common.base_client import ApiClient
from api_tests.tla.routes.path import APIPath
from api_tests.tla.routes.query import APIQuery


class ClientBase:
    """
    Общий класс для запросов к эндпоинтам API.

    Атрибуты
    --------
    client : ApiClient
        Объект клиента для выполнения HTTP-запросов.
    path : type(APIPath)
        Путь к ресурсу API, который будет использоваться для запросов.
    base_params : dict
        Словарь с базовыми параметрами, которые будут использоваться
         в каждом запросе.
    """

    def __init__(
            self,
            client: ApiClient,
            path: type(APIPath),
            base_params: dict
    ):
        self.client = client
        self.path = path
        self.base_params = base_params

    def get(self, params: dict) -> Response:
        """
         Общий метод для выполнения GET-запроса с указанными параметрами.

         Параметры
         ----------
         params : dict
             Словарь параметров запроса. Ключи - имена параметров,
              значения - их значения.
             Если значение параметра равно None, параметр будет
              включен в строку запроса без значения.

         Возвращает
         ----------
         Response
             Ответ на HTTP-запрос, объект класса Response от
              библиотеки requests.

         Пример
         -------
         params = {"id": 4097, "state": None, "msource": backMegapolisUrl}
         В итоге будут сформированы параметры пути:
          params_string = lights?id=4097&state&msource=backMegapolisUrl

          В итогу будет сделан запрос:
           http://traffic-lights-api-develop.k8.sccloud.ru/
           lights?id=4097&state=null&msource=backMegapolisUrl
         """
        params_string = "&".join(
            [f"{key}={value}" if value is not None else key for key, value in
             params.items()]
        )
        return self.client.get(
            path=self.path,
            params=params_string
        )

    def get_updated_params(
            self, additional_params: dict[str, int | str]
    ) -> dict[str, int | str]:
        """Добавляет новые параметры к базовым."""
        new_params = self.base_params.copy()
        new_params.update(additional_params)
        return new_params

    def get_full_or_all_objs(
            self, ids: str
    ) -> Response:
        """
         Получает объекты на основе заданных параметров.

         Параметры:
         ----------
         ids : str
             Идентификаторы расписаний. Может быть 'full' или 'all'.

         Возвращает:
         -----------
         Response
             Объект ответа, содержащий данные.

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
