from sqlalchemy import Column, String, Boolean, BigInteger, Numeric
from sqlalchemy.dialects.postgresql import UUID, JSONB

from core.db import Base


class TrafficLightsObjects(Base):
    __tablename__ = 'TrafficLights_Objects'
    id = Column('id', UUID(as_uuid=True), primary_key=True)
    ext_id = Column('extId', String, nullable=False)
    tdk = Column('tdk', String, nullable=False)
    tdk_name = Column('tdkName', String, nullable=False)
    state_name = Column('stateName', String, nullable=False)
    street_1 = Column('street1', String, nullable=False)
    street_2 = Column('street2', String, nullable=False)
    mag = Column('mag', String, nullable=False)
    longitude = Column('longitude', Numeric, nullable=False)
    latitude = Column('latitude', Numeric, nullable=False)
    way = Column('way', BigInteger, nullable=True)
    time_rcv = Column('time_rcv', BigInteger, nullable=False)
    creation_time = Column('creationTime', BigInteger, nullable=False)
    update_time = Column('updateTime', BigInteger, nullable=False)
    coordinates = Column('coordinates', String, nullable=False)
    has_detector = Column('hasDetector', Boolean, nullable=True)
    has_controller = Column('hasController', Boolean, nullable=False)
    sfs_id = Column('sfsId', String, nullable=True)
    previous_value = Column('previousValue', JSONB, nullable=True)
    state = Column('state', String, nullable=True)
    creation_author = Column(
        'creationAuthor', UUID(as_uuid=True), nullable=True
    )
    update_author = Column('updateAuthor', UUID(as_uuid=True), nullable=True)
    is_active = Column('isActive', Boolean, nullable=False)
    ext = Column('ext', String, nullable=True)
    attached_files = Column('attachedFiles', JSONB, nullable=True)
    link = Column('link', String, nullable=True)
    type = Column('type', String, nullable=True)
    update_time_data = Column('updateTimeData', BigInteger, nullable=False)
    mo_id = Column('moId', UUID(as_uuid=True), nullable=True)
    source = Column('source', String, nullable=False)
    msource = Column('msource', String, nullable=False)
    mode = Column('mode', String, nullable=True)
    ext_mode = Column('extMode', String, nullable=True)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in
            self.__table__.columns
        }
