from morfdict import StringDict
from sqlalchemy import create_engine

from pluton.plug.app_plug import AppPlug


class SqlAlchemyPlug(AppPlug):

    def _morf_sql_url(self, obj, value):
        if obj['type'] == 'sqlite':
            value = 'sqlite:///%(paths:sqlite_db)s'
        else:
            value = (
                '%(type)s://%(login)s:%(password)s@%(host)s:%(port)s/'
                '%(name)s'
            )
        return value % obj

    def populate_default_settings(self):
        dbsettings = StringDict()
        dbsettings['url'] = ''
        dbsettings.set_morf('url', self._morf_sql_url)
        self.parent.settings['db'] = dbsettings

    def generate_registry(self, registry):
        engine = create_engine(self.parent.settings['db:url'])
        registry['db_engine'] = engine
