from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from uuid import uuid4

from pluton.plug.sqlalchemy.model import Model


class Client(Model):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    api_key = Column(String, nullable=False, default=lambda: str(uuid4()))
    api_secret = Column(String, nullable=False, default=lambda: str(uuid4()))
