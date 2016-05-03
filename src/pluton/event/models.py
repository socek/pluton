from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from pluton.plug.sqlalchemy.model import Model


class EventGroup(Model):
    __tablename__ = 'event_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    arg = Column(String)
    state = Column(String, nullable=False, default='normal')
    is_hidden = Column(Boolean, default=False)
    reaction_data = Column(JSON)
    description = Column(String)

    endpoint_id = Column(Integer, ForeignKey('endpoints.id'), nullable=False)
    endpoint = relationship('Endpoint')


class Event(Model):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    raw = Column(JSON)

    group_id = Column(Integer, ForeignKey('event_groups.id'), nullable=False)
    group = relationship('EventGroup')

    when_created = Column(DateTime, default=datetime.utcnow)
