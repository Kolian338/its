from api_tests.tla.api.lights import LightsClient


def test_get_light_extend_state(lights: LightsClient):
    """
    Получение расширенного состояния только одного светофорного объекта.
    """
    response = lights.get_light_extend_state(id='4097')
    print(response.json())

    assert response.status_code == 200
