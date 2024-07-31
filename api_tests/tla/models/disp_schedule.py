from sqlalchemy import Column, String, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import UUID, JSONB

from core.db import Base


class TrafficLightsDispShedule(Base):
    __tablename__ = 'TrafficLights_Dispshedule'
    id = Column('id', UUID(as_uuid=True), primary_key=True)
    guid = Column('guid', String, nullable=False)
    caption = Column('caption', String, nullable=True)
    time_on = Column('timeOn', DateTime(timezone=True), nullable=False)
    time_off = Column('timeOff', DateTime(timezone=True), nullable=False)
    type = Column('type', String, nullable=False)
    type_name = Column('typeName', String, nullable=False)
    objs = Column('objs', JSONB, nullable=False)
    creation_time = Column('creationTime', BigInteger, nullable=False)
    update_time = Column('updateTime', BigInteger, nullable=False)
    creation_author = Column('creationAuthor', UUID(as_uuid=True),
                             nullable=True)
    update_author = Column('updateAuthor', UUID(as_uuid=True), nullable=True)
    green_route_ids = Column('greenRouteIds', JSONB, nullable=True)
    mo_id = Column('moId', UUID(as_uuid=True), nullable=True)
    source = Column('source', String, nullable=False)
    msource = Column('msource', String, nullable=False)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in
            self.__table__.columns
        }
