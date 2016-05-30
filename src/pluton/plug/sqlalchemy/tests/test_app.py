from pluton.application.testing import PlugableCase

from ..app import SqlAlchemyPlug


class TestSqlAlchemyPlug(PlugableCase):
    _object_cls = SqlAlchemyPlug

    def test_morf_sql_url_for_sqlite(self):
        data = {
            'type': 'sqlite',
            'paths:sqlite_db': 'path_to_sqlite_db',
        }
        result = self.object()._morf_sql_url(data, None)
        assert result == 'sqlite:///path_to_sqlite_db'

    def test_morf_sql_url_for_postgresql(self):
        data = {
            'type': 'postgresql',
            'login': 'login',
            'password': 'password',
            'host': 'host',
            'port': 'port',
            'name': 'name',
        }
        result = self.object()._morf_sql_url(data, None)
        assert result == 'postgresql://login:password@host:port/name'
