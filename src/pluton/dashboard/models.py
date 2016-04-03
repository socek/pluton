from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from pluton.plug.sqlalchemy.model import Model


class Client(Model):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
