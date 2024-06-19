from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Класс для настроек проектов.

    itec_url: url для сервиса itec
    tla_url: url для сервиса lta
    По умолчанию заданы дефолтные url на случай если в .env их нет.
    """

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    itec_url: str = 'http://192.168.32.67:3000'
    tla_url: str = 'http://traffic-lights-api-develop.k8.sccloud.ru'
    msource: str = 'backMegapolisUrl2'


base_settings = Settings()
