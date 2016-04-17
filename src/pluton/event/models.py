from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON

from pluton.plug.sqlalchemy.model import Model


class Event(Model):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    raw = Column(JSON)
    state = Column(String, nullable=False, default='normal')

    when_created = Column(DateTime, default=datetime.utcnow)

    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    client = relationship('Client')
