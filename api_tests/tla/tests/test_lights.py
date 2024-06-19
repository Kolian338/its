import requests
from api_tests.tla.api.lights import get_lights


def test_get_lights(client):
    response = get_lights(client=client)
    print(response.json())

    assert response.status_code == 200
