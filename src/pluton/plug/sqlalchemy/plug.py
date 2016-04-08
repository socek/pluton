from sqlalchemy.orm import sessionmaker

from pluton.plug.plug import Plug


class DatabasePlug(Plug):

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
        db = self.registry['db']
        db.expire_all()
        return db
