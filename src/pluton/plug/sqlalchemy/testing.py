from pluton.plug.testing.cache import cache
from pluton.plug.testing.case import BasePlugableCase

from .plug import DatabasePlug


class BaseDatabaseCase(BasePlugableCase):

    def create_plugs(self):
        super().create_plugs()
        self.database = self.add_plug(DatabasePlug)

    @cache
    def object(self, *args, **kwargs):
        obj = super().object(*args, **kwargs)
        self._regenerate_table(obj)
        return obj

    def _regenerate_table(self, obj):
        obj.model.metadata.create_all(self.registry['db_engine'])

    def reset_table(self):
        self.object().find_all().delete()
