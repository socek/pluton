from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.ext.declarative import declarative_base

from pluton.plug.plug import Plug

DeclarativeBase = declarative_base()


class Model(AbstractConcreteBase, DeclarativeBase, Plug):

    def __repr__(self):
        id_ = str(self.id) if getattr(self, 'id', None) else 'None'
        return '%s (%s)' % (self.__class__.__name__, id_)
