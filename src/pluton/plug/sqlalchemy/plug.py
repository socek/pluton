from sqlalchemy.orm import sessionmaker

from pluton.plug.plug import Plug


class DatabasePlug(Plug):

    def feed_parent(self, parent):
        super().feed_parent(parent)
        if 'expire_all' not in self.request_cache:
            # we want to do expire_all only once per request
            db = self()
            db.commit()
            db.expire_all()
            self.request_cache['expire_all'] = True

    def __call__(self):
        return self._get_database()

    def _get_database(self):
        if not getattr(self, 'db', None):
            engine = self.registry['db_engine']
            self.db = sessionmaker(bind=engine)()
        return self.db
