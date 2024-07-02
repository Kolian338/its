import allure
from jsonschema import validate


@allure.step('Проверка схемы')
def validate_schema(instance: dict, schema: dict) -> None:
    validate(instance=instance, schema=schema)
