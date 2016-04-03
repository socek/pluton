from sqlalchemy.orm.exc import NoResultFound

from pluton.plug.plug import Plug
from .plug import DatabasePlug


class Driver(Plug):

    def create_plugs(self):
        self.database = self.add_plug(DatabasePlug)

    @property
    def query(self):
        return self.database().query


class ModelDriver(Driver):

    def upsert(self, **kwargs):
        try:
            return self.find_by(**kwargs).one()
        except NoResultFound:
            return self.create(**kwargs)

    def get_by_id(self, id):
        return self.find_all().filter_by(id=id).one()

    def find_all(self):
        return self.query(self.model)

    def find_by(self, **kwargs):
        return self.query(self.model).filter_by(**kwargs)

    def create(self, **kwargs):
        obj = self.model()
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.database().add(obj)
        return obj

    def delete_by_id(self, id_):
        self.delete(self.get_by_id(id_))

    def delete(self, obj):
        self.database().delete(obj)

    def _append_metadata(self, metadatas):
        metadatas.add(self.model.metadata)

    def update(self, instance):
        self.database().merge(instance)
        self.database().flush()
