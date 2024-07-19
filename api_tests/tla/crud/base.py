from sqlalchemy import select

from core.db import AsyncSessionPg


class CRUDBase:

    def __init__(self, model):
        self.model = model

    async def get_by_attribute(
            self,
            attr_name: str,
            attr_value: str,
            session: AsyncSessionPg,
    ):
        """Получить объект по атрибуту."""
        attr = getattr(self.model, attr_name)
        db_obj = await session.execute(
            select(self.model).where(attr == attr_value)
        )
        return db_obj.scalars().first()

    async def get_multi(
            self,
            session: AsyncSessionPg
    ):
        """Получить все объекты заданного класса"""
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def create(
            self,
            obj_in,
            session: AsyncSessionPg
    ):
        """Создать новый объект"""
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
            self,
            db_obj,
            obj_in,
            session: AsyncSessionPg
    ):
        """Обновить объект."""
        obj_data = db_obj.to_dict()
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
            self,
            db_obj,
            session: AsyncSessionPg
    ):
        """Удалить объект."""
        await session.delete(db_obj)
        await session.commit()
        return db_obj
