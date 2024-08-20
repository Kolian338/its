from api_tests.tla.api.endpoints.lights import LightsClient
from api_tests.tla.assertions.base import validate_response
from api_tests.tla.fixtures.base import create_api_client
from api_tests.tla.routes.path import APIPath
from api_tests.tla.schemas.response.lights import (
    LightStateResponse,
)


def get_all_id_from_lights() -> list[int]:
    """Функция возвращающая все id существующих СО."""
    client = create_api_client(LightsClient, APIPath.LIGHTS)
    response = client.get_lights_state()
    validated_obj = validate_response(response, LightStateResponse)
    ids = [item.id for item in validated_obj.info]
    return ids
