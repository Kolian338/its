from api_tests.tla.constants import ResponseBody


def result_must_be_accepted(value: str):
    if value != ResponseBody.DELETED:
        raise ValueError(f'Значение должно быть {ResponseBody.DELETED}')
    return value
