from sqlalchemy.orm import sessionmaker

from pluton.plug.plug import Plug


class DatabasePlug(Plug):

    def feed_parent(self, parent):
        super().feed_parent(parent)
        if 'expire_all' not in self.request_cache:
            # we want to do expire_all only once per request
            self().commit()
            self().expire_all()
            self.request_cache['expire_all'] = True

    def __call__(self):
        if self.settings['db']['type'] == 'sqlite':
            return self._get_sqlite_database()
        else:
            return self._get_normal_database()

    def _get_sqlite_database(self):
        if not getattr(self, 'db', None):
            engine = self.registry['db_engine']
            self.db = sessionmaker(bind=engine)()
        return self.db

    def _get_normal_database(self):
        return self.registry['db']
