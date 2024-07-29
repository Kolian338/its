import allure
import pytest

from api_tests.tla.api.api_client import client_api
from api_tests.tla.api.endpoints.dispshedule import DispScheduleClient
from api_tests.tla.routes.path import APIPath
from api_tests.tla.routes.query import APIQuery
from api_tests.tla.schemas.request.dispshedule import DispSheduleRequest


@pytest.fixture
@allure.title('API клиент для запросов к /dispshedule.')
def disp_schedule_client() -> DispScheduleClient:
    return DispScheduleClient(
        client=client_api(),
        path=APIPath.DISP_SCHEDULE,
        base_params={
            APIQuery.MSOURCE: APIQuery.BACKMEGAPOLISURL,
        }
    )


@pytest.fixture
@allure.title('Создаение объекта дисп.раписания.')
def disp_schedule_data():
    return DispSheduleRequest()
