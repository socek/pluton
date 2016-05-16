import sys

from bael.project.develop import Develop
from bael.project.virtualenv import BaseVirtualenv
from baelfire.dependencies import AlwaysRebuild
from baelfire.dependencies import RunBefore
from baelfire.error import CommandAborted
from baelfire.error import CommandError

from .alembic import AlembicUpgrade


class PlutonSettingsMixin(object):

    def phase_settings(self):
        super().phase_settings()
        self.settings['ignore_inits_dirs'] = self.settings.get(
            'ignore_inits_dirs', [])
        self.settings['ignore_inits_dirs'].append('templates')
        self.settings['ignore_inits_dirs'].append('static')


class PlutonDevelop(PlutonSettingsMixin, Develop):
    pass


class Serve(BaseVirtualenv):

    def phase_settings(self):
        super().phase_settings()
        self.paths.set_path('exe:pserve', 'virtualenv:bin', 'pserve')

    def create_dependecies(self):
        self.add_dependency(RunBefore(AlembicUpgrade()))
        self.add_dependency(AlwaysRebuild())

    def build(self):
        try:
            self.popen(
                ['%(exe:pserve)s %(frontendini)s --reload' % self.paths],
            )
        except CommandAborted:
            self.logger.info('Aborted')


class Shell(BaseVirtualenv):

    def phase_settings(self):
        super().phase_settings()
        self.paths.set_path('exe:pshell', 'virtualenv:bin', 'pshell')

    def create_dependecies(self):
        self.add_dependency(RunBefore(AlembicUpgrade()))
        self.add_dependency(AlwaysRebuild())

    def build(self):
        try:
            self.popen(
                ['%(exe:pshell)s %(frontendini)s' % self.paths],
            )
        except CommandAborted:
            self.logger.info('Aborted')


class BasePyTest(BaseVirtualenv):

    def create_dependecies(self):
        self.add_dependency(RunBefore(AlembicUpgrade()))
        self.add_dependency(AlwaysRebuild())

    def pytest(self, command='', *args, **kwargs):
        kwargs['shell'] = True
        kwargs['cwd'] = self.paths['package']['main']
        command = self.paths['exe:pytest'] + ' ' + command
        return self.popen([command], *args, **kwargs)


class RunTests(BasePyTest):

    def build(self):
        cmd = " ".join(
            '"%s"' % x.strip().replace('"', r'\"')
            for x in sys.argv[1:]
        )
        try:
            self.pytest(cmd)
        except (CommandAborted, CommandError):
            pass


class RunCoverage(BasePyTest):

    def build(self):
        cmd = " ".join(
            '"%s"' % x.strip().replace('"', r'\"')
            for x in sys.argv[1:]
        )
        try:
            self.pytest('--cov pluton ' + cmd)
        except (CommandAborted, CommandError):
            pass
