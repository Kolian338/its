import allure
import pytest_asyncio

from api_tests.tla.api.api_client import client_api
from api_tests.tla.api.endpoints.base import ClientBase
from api_tests.tla.routes.query import APIQuery
from core.db import AsyncSessionPg


@allure.title('Создается асинхронный генератор сессий.')
@pytest_asyncio.fixture
async def get_async_session():
    async with AsyncSessionPg() as async_session:
        yield async_session


def create_api_client(client_class, path) -> type(ClientBase):
    """
    Создает API клиент с заданными параметрами.

    Параметры:
    ----------
    client_class : type
        Класс клиента API.
    path : str
        Путь API.

    Возвращает:
    -----------
    ClientBase
        Экземпляр клиента API.
    """
    return client_class(
        client=client_api(),
        path=path,
        base_params={
            APIQuery.MSOURCE: APIQuery.BACKMEGAPOLISURL,
        }
    )
