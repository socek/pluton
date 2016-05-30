from mock import MagicMock
from mock import patch

from pluton.application.testing import PlugableCase
from pluton.plug.testing.cache import cache

from ..plug import DatabasePlug


class TestDatabasePlug(PlugableCase):
    _object_cls = DatabasePlug

    @cache
    def mcall(self):
        return self.pobject(self._object_cls, '__call__')

    @cache
    def msettings(self):
        return self.pdict(self.object().settings, {}, clear=True)

    @cache
    def mget_sqlite_database(self):
        return self.pobject(self.object(), '_get_sqlite_database')

    @cache
    def mget_normal_database(self):
        return self.pobject(self.object(), '_get_normal_database')

    @cache
    def msessionmaker(self):
        return self.patch('pluton.plug.sqlalchemy.plug.sessionmaker')

    def test_feed_parent(self):
        mcall = self.mcall()

        self.object()

        mcall.return_value.commit.assert_called_once_with()
        mcall.return_value.expire_all.assert_called_once_with()
        mcall.assert_called_once_with()

        assert self.request_cache == {'expire_all': True}

    def test_call(self):
        settings = {
            'db': {
                'type': 'sqlite',
            }
        }
        msqlite = self.mget_sqlite_database()
        mdb = self.mget_normal_database()
        with patch.dict(self.object().settings, settings, clear=True):
            assert self.object()() == msqlite.return_value
            msqlite.assert_called_once_with()

        settings['db']['type'] = 'postgresql'

        with patch.dict(self.object().settings, settings, clear=True):
            assert self.object()() == mdb.return_value
            mdb.assert_called_once_with()

    def test_get_sqlite_database(self):
        db_engine = MagicMock()
        registry = {
            'db_engine': db_engine,
        }
        msm = self.msessionmaker()

        with patch.dict(self.object().registry, registry, clear=True):
            db = self.object()._get_sqlite_database()
        msm.assert_called_once_with(bind=db_engine)
        msm.return_value.assert_called_once_with()
        assert db == msm.return_value.return_value

        with patch.dict(self.object().registry, registry, clear=True):
            db = self.object()._get_sqlite_database()
        msm.assert_called_once_with(bind=db_engine)
        msm.return_value.assert_called_once_with()
        assert db == msm.return_value.return_value

    def test_get_normal_database(self):
        db = MagicMock()
        registry = {
            'db': db,
        }
        with patch.dict(self.object().registry, registry, clear=True):
            assert self.object()._get_normal_database() == db
