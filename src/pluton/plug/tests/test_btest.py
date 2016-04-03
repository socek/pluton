from impaf.testing.btest import BaseFixtures
from impaf.testing.btest import TestCase
from impaf.testing.btest import WithFixtures
# from impaf.testing.btest import Fixture
from impaf.testing.cache import ClassCache


class TestMyTest(TestCase):

    def test_one(self):
        assert True

    def test_two(self):
        assert True


class FixtureDriver(BaseFixtures):

    @ClassCache()
    def one(self):
        print('one')
        return 'elo'

    def two(self):
        return 'two'


class FixtureDriverTwo(BaseFixtures):

    @ClassCache()
    def two(self):
        print('one')
        return 'elo'


class TestMySecondTest(TestCase):
    Fixtures = FixtureDriver

    @WithFixtures()
    def test_two(self, fixtures):
        print('a')
        fixtures.one()
        fixtures.one()

    @WithFixtures(fixtures=FixtureDriverTwo)
    def test_second(self, fixtures):
        print('b')
        fixtures.two()
        fixtures.two()
