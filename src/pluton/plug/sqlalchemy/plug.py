from sqlalchemy.orm import sessionmaker

from pluton.plug.plug import RequestPlug


class DatabasePlug(RequestPlug):

    def __call__(self):
        if not getattr(self.main, '_database', None):
            if self.settings['db']['type'] == 'sqlite':
                self.main._database = self._get_sqlite_database()
            else:
                self.main._database = self._get_normal_database()
        return self.main._database

    def _get_sqlite_database(self):
        engine = self.registry['db_engine']
        return sessionmaker(bind=engine)()

    def _get_normal_database(self):
        db = self.registry['db']
        db.expire_all()
        return db
