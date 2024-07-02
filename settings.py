from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum
from pydantic import Field


class MsourceEnum(str, Enum):
    BACKMEGAPOLISURL2 = 'backMegapolisUrl2'
    BACKMEGAPOLISURL = 'backMegapolisUrl'


class Settings(BaseSettings):
    """Общий класс настроек."""

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.',
        extra='allow'
    )
    path: str


class ItecSettings(Settings):
    """
    Класс для настроек проектов.

    По приоритету берется из .env.
    По умолчанию заданы дефолтные url в атрибутах,
    на случай если в .env их нет.
    """

    itec_url: str = Field(
        'http://192.168.32.67:3000',
        description='url для сервиса itec'
    )


class TlaSettings(Settings):
    """
    Класс для настроек проектов.

    По приоритету берется из .env.
    По умолчанию заданы дефолтные url в атрибутах,
    на случай если в .env их нет.
    """

    tla_url: str = Field(
        'http://traffic-lights-api-develop.k8.sccloud.ru',
        description='url для сервиса tla'
    )
    msource: str = Field(
        MsourceEnum.BACKMEGAPOLISURL2,
        description=(
            'адрес для запросов от TLA в Мегаполис из конфига:'
            'https://gitlab.sccloud.ru/dis'
            '/traffic-lights-api/-/blob/develop/config.toml'
        )
    )


itec_settings = ItecSettings()
tla_settings = TlaSettings()
