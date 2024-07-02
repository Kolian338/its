import allure

from api_tests.tla.api.lights import LightsClient
from api_tests.tla.assertions.schema import validate_schema
from api_tests.tla.schemas.light import LightStateResponse


def test_get_light_extend_state(lights_client: LightsClient):
    """
    Получение расширенного состояния только одного светофорного объекта.
    """
    response = lights_client.get_light_extend_state(id='4097')
    print(response.json())

    assert response.status_code == 200


@allure.title('Получение состояния светофорного объекта.')
def test_get_light_state(lights_client: LightsClient):
    """
    Получение состояния только одного светофорного объекта.
    """
    response = lights_client.get_light_state(id='4097')
    print(response.json())

    assert response.status_code == 200
    validate_schema(
        response.json(), LightStateResponse.model_json_schema()
    )
