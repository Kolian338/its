from http import HTTPStatus

import allure
from jsonschema import validate
from pydantic import BaseModel
from requests import Response


def validate_schema(instance: dict, schema: dict) -> None:
    validate(instance=instance, schema=schema)


@allure.step('Валидация объекта и схемы')
def validate_success_response(
        response: Response, schema_class: type(BaseModel)
) -> None:
    # Валидация объекта внутренними валидаторами класса
    schema_class(**response.json())
    # Дополнительная валидация схемы
    validate_schema(
        response.json(), schema_class.model_json_schema()
    )
    assert response.status_code == HTTPStatus.OK
