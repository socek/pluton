from mock import MagicMock
from sqlalchemy.orm.exc import NoResultFound

from pluton.application.testing import PlugableCase
from pluton.plug.testing.cache import cache

from ..driver import ModelDriver


class ExampleModelDriver(ModelDriver):
    model = MagicMock()


class TestModelDriver(PlugableCase):
    _object_cls = ExampleModelDriver

    @cache
    def mdatabase(self):
        return self.pobject(self.object(), 'database')

    @property
    def model(self):
        return self.object().model

    @cache
    def mcreate(self):
        return self.pobject(self.object(), 'create')

    @cache
    def mget_by_id(self):
        return self.pobject(self.object(), 'get_by_id')

    def test_upsert_on_existing(self):
        mdb = self.mdatabase()

        result = self.object().upsert(data='data')

        assert result == (
            mdb.return_value
            .query.return_value
            .filter_by.return_value
            .one.return_value
        )
        mdb.assert_called_once_with()
        mdb.return_value.query.assert_called_once_with(self.model)
        (
            mdb.return_value
            .query.return_value
            .filter_by.assert_called_once_with(data='data')
        )
        (
            mdb.return_value
            .query.return_value
            .filter_by.return_value
            .one.assert_called_once_with()
        )

    def test_upsert_non_existing(self):
        mdb = self.mdatabase()
        mcreate = self.mcreate()

        (
            mdb.return_value
            .query.return_value
            .filter_by.return_value
            .one.side_effect
        ) = NoResultFound()

        result = self.object().upsert(data='data')

        assert result == mcreate.return_value
        mdb.assert_called_once_with()
        mdb.return_value.query.assert_called_once_with(self.model)
        (
            mdb.return_value
            .query.return_value
            .filter_by.assert_called_once_with(data='data')
        )
        (
            mdb.return_value
            .query.return_value
            .filter_by.return_value
            .one.assert_called_once_with()
        )

    def test_get_by_id(self):
        mdb = self.mdatabase()

        result = self.object().get_by_id('myid')

        assert result == (
            mdb.return_value
            .query.return_value
            .filter_by.return_value
            .one.return_value
        )
        mdb.assert_called_once_with()
        mdb.return_value.query.assert_called_once_with(self.model)
        (
            mdb.return_value
            .query.return_value
            .filter_by.assert_called_once_with(id='myid')
        )
        (
            mdb.return_value
            .query.return_value
            .filter_by.return_value
            .one.assert_called_once_with()
        )

    def test_find_all(self):
        mdb = self.mdatabase()

        result = self.object().find_all()

        assert result == (
            mdb.return_value
            .query.return_value
        )
        mdb.assert_called_once_with()
        mdb.return_value.query.assert_called_once_with(self.model)

    def test_find_by(self):
        mdb = self.mdatabase()

        result = self.object().find_by(something='mysomething')

        assert result == (
            mdb.return_value
            .query.return_value
            .filter_by.return_value
        )
        mdb.assert_called_once_with()
        mdb.return_value.query.assert_called_once_with(self.model)
        (
            mdb.return_value
            .query.return_value
            .filter_by.assert_called_once_with(something='mysomething')
        )

    def test_delete_by_id(self):
        mdb = self.mdatabase()
        mget = self.mget_by_id()

        self.object().delete_by_id('deletable_id')

        mget.assert_called_once_with('deletable_id')
        mdb.return_value.delete.assert_called_once_with(mget.return_value)
        mdb.assert_called_once_with()

    def test_update(self):
        mdb = self.mdatabase()
        instance = MagicMock()

        self.object().update(instance)
        mdb.return_value.merge.assert_called_once_with(instance)
        mdb.return_value.flush.assert_called_once_with()
        mdb.assert_called_once_with()

    def test_create(self):
        mdb = self.mdatabase()

        result = self.object().create(something='arg')

        assert result == self.model.return_value
        mdb.return_value.add.assert_called_once_with(result)
        mdb.assert_called_once_with()
        assert result.something == 'arg'
