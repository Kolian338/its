from sqlalchemy import Column, String, ForeignKey, BigInteger, orm
from sqlalchemy.dialects.postgresql import UUID, JSONB

from core.db import Base


class TrafficLightsSignalPrograms(Base):
    __tablename__ = 'TrafficLights_SignalPrograms'
    id = Column('id', UUID(as_uuid=True), primary_key=True)
    ido = Column('ido', String, nullable=False)
    ast = Column('ast', String, nullable=True)
    bcycle = Column('bcycle', BigInteger, nullable=True)
    cycle = Column('cycle', BigInteger, nullable=True)
    num = Column('num', String, nullable=True)
    bast = Column('bast', String, nullable=True)
    lens = Column('lens', JSONB, nullable=True)
    blens = Column('blens', JSONB, nullable=True)
    phases = Column('phases', JSONB, nullable=True)
    creation_time = Column('creationTime', BigInteger, nullable=False)
    update_time = Column('updateTime', BigInteger, nullable=False)
    creation_author = Column(
        'creationAuthor', UUID(as_uuid=True), nullable=True
    )
    update_author = Column(
        'updateAuthor', UUID(as_uuid=True), nullable=True
    )
    source = Column('source', String, nullable=False)
    msource = Column('msource', String, nullable=False)
    traffic_light_id = Column(
        'trafficLightId',
        UUID(as_uuid=True),
        ForeignKey('TrafficLights_Objects.id')
    )
    lights_object = orm.relationship(
        "TrafficLightsObjects", backref="TrafficLights_SignalPrograms"
    )
