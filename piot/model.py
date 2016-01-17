from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SensorReading(Base):
    __tablename__ = 'sensorreading'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    sensortype = Column(String)
    timestamp = Column(DateTime)

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
        'polymorphic_on': sensortype
    }

    def __repr__(self):
        return 'SensorReading(name=\'%s\', value=\'%s\', unit=\'%s\')' \
            % (self.name, self.value, self.unit)


class AnalogSensorReading(SensorReading):
    __tablename__ = 'analogsensorreading'

    id = Column(Integer, ForeignKey('sensorreading.id'), primary_key=True)
    value = Column(Numeric(precision=6, scale=2))
    unit = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'analogsensorreading',
    }


class DigitalSensorReading(SensorReading):
    __tablename__ = 'digitalsensorreading'

    id = Column(Integer, ForeignKey('sensorreading.id'), primary_key=True)
    value = Column(Boolean)

    __mapper_args__ = {
        'polymorphic_identity': 'digitalsensorreading',
    }


class NotificationEvent(Base):
    __tablename__ = 'notificationevent'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)