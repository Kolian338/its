from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum


class MsourceEnum(str, Enum):
    BACKMEGAPOLISURL = 'backMegapolisUrl'
    BACKMEGAPOLISURL2 = 'backMegapolisUrl2'


class Settings(BaseSettings):
    """Общий класс настроек."""

    model_config = SettingsConfigDict(
        env_file='../.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.',
        extra='ignore'
    )
    path: str
    url: str


class ItecSettings(Settings):
    """
    Класс для настроек Itec.

    По приоритету берется из .env.
    По умолчанию заданы дефолтные url в атрибутах,
    на случай если в .env их нет.
    """

    url: str = 'http://192.168.32.67:3000'


class TlaSettings(Settings):
    """
    Класс для настроек TLA.

    По приоритету берется из .env.
    По умолчанию заданы дефолтные url в атрибутах,
    на случай если в .env их нет.
    """

    url: str = 'http://traffic-lights-api-develop.k8.sccloud.ru'
    msource: str = MsourceEnum.BACKMEGAPOLISURL2
    pg_url: str = (
        'postgresql+asyncpg:'
        '//postgres:9Jd7HiH2AE5pLtS_@192.168.32.79:5432/develop_its'
    )


itec_settings = ItecSettings()
tla_settings = TlaSettings()
