from api_tests.tla.api.lights import get_lights
from api_tests.common.base_client import ApiClient


def test_get_lights(client: ApiClient):
    response = get_lights(client=client)
    print(response.json())


    assert response.status_code == 200
