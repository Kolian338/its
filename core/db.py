from sqlalchemy.ext.asyncio import (create_async_engine, AsyncSession)
from sqlalchemy.orm import (declarative_base, sessionmaker)

from core.config import tla_settings

engine = create_async_engine(tla_settings.pg_url, echo=True)

AsyncSessionPg = sessionmaker(engine, class_=AsyncSession)

Base = declarative_base()  # Базовый класс для будующих моделей
