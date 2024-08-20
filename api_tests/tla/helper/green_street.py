from api_tests.tla.schemas.request.green_street import AddGreenRouteRequest


def update_route_with_part_guid(
        green_street_rout_data: AddGreenRouteRequest, part_guid: str
):
    """Обновляет маршрут с использованием GUID созданного участка."""
    green_street_rout_data.add_green_rout[0].parts[0].guid = part_guid
