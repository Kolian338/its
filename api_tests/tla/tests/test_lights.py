import allure
import pytest

from api_tests.tla.api.endpoints.lights import LightsClient
from api_tests.tla.assertions.base import validate_response
from api_tests.tla.helper.lights import get_all_id_from_lights
from api_tests.tla.schemas.response.lights import (
    LightStateResponse, SignalProgramResponse
)


@pytest.mark.asyncio
@allure.feature('Lights')
@allure.story('Lights API')
class TestState:
    @allure.title(
        'Получение состояния одного/нескольких светофорных объектов.'
    )
    @pytest.mark.parametrize(
        'id',
        (4097, get_all_id_from_lights(),),
    )
    def test_get_light_state(
            self,
            id: int,
            lights_client: LightsClient,
    ):
        response = lights_client.get_lights_state(id)
        validate_response(response, LightStateResponse)

    @allure.title(
        'Получение состояния списка светофорных объектов.'
    )
    def test_get_all_lights(
            self,
            lights_client: LightsClient,
    ):
        response = lights_client.get_lights_state()
        validate_response(response, LightStateResponse)


@pytest.mark.asyncio
class TestSignalProgram:
    @allure.title(
        'Получение сигнальных программ СО.'
    )
    @pytest.mark.parametrize(
        'id',
        (4098, get_all_id_from_lights(),)
    )
    def test_get_light_signal_program(
            self,
            id: int,
            lights_client: LightsClient,
    ):
        response = lights_client.get_signal_program(id)
        validate_response(response, SignalProgramResponse)

    @allure.title(
        'Получение полного списка текущих сигнальных программ CО.'
    )
    def test_get_all_signal_programs(
            self,
            lights_client: LightsClient,
    ):
        response = lights_client.get_signal_program()
        validate_response(response, SignalProgramResponse)
