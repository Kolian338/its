import allure
import pytest

from api_tests.tla.api.endpoints.dispshedule import DispScheduleClient
from api_tests.tla.fixtures.base import create_api_client
from api_tests.tla.routes.path import APIPath
from api_tests.tla.schemas.request.disp_shedule import DispSheduleRequest


@pytest.fixture
@allure.title('API клиент для запросов к /dispshedule.')
def disp_schedule_client() -> DispScheduleClient:
    return create_api_client(DispScheduleClient, APIPath.DISP_SCHEDULE)


@pytest.fixture
@allure.title('Создаение объекта дисп.раписания.')
def disp_schedule_data() -> DispSheduleRequest:
    return DispSheduleRequest()
