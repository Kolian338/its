import allure
from jsonschema import validate
from pydantic import BaseModel
from requests import Response


def validate_schema(
        instance: dict, schema: dict
) -> None:
    """
    Валидирует JSON-объект на основе заданной JSON-схемы.

    Аргументы:
        instance (dict): JSON-объект для валидации.
        schema (dict): JSON-схема для валидации.

    Исключения:
        jsonschema.exceptions.ValidationError:
         Если JSON-объект не соответствует схеме.
    """
    validate(instance=instance, schema=schema)


@allure.step('Валидация объекта.')
def validate_object(
        response: Response,
        schema_class: type(BaseModel)
) -> type(BaseModel):
    """
    Валидирует объект ответа на основе заданного класса схемы Pydantic.

    Аргументы:
        response (Response): HTTP-ответ для валидации.
        schema_class (type(BaseModel)): Класс схемы Pydantic для валидации.

    Возвращает:
        BaseModel: Экземпляр класса схемы, заполненный данными из ответа.
    """
    validated_object = schema_class(**response.json())
    return validated_object


@allure.step('Валидация схемы ответа.')
def validate_response(
        response: Response,
        schema_class: type(BaseModel)
) -> type(BaseModel):
    """
    Валидирует объект ответа и его схему на основе заданного
     класса схемы Pydantic.

    Аргументы:
        response (Response): HTTP-ответ для валидации.
        schema_class (type(BaseModel)): Класс схемы Pydantic для валидации.

    Возвращает:
        BaseModel: Экземпляр класса схемы, заполненный данными из ответа.
    """
    validated_object = validate_object(
        response, schema_class
    )
    validate_schema(
        response.json(), schema_class.model_json_schema()
    )
    return validated_object
