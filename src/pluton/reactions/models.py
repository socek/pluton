from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from pluton.plug.sqlalchemy.model import Model


class ReactionLink(Model):
    __tablename__ = 'reaction_links'

    id = Column(Integer, primary_key=True)
    priority = Column(Integer, nullable=False, default=0)
    reaction_name = Column(String, nullable=False)
    event_name = Column(String, nullable=False)

    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    client = relationship('Client')
