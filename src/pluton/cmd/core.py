import pluton

from bael.project.core import ProjectCore
from os.path import dirname
from pluton.application.app import main


class PlutonCore(ProjectCore):

    def before_dependencies(self):
        super().before_dependencies()

        main._generate_settings({}, endpoint='command')

        self.settings.update(main.settings)
        self.paths.update(main.paths)
        self.paths['cwd'] = dirname(dirname(dirname(pluton.__file__)))
        self.paths.set_path('package:src', 'cwd', 'src')
        self.paths.set_path('package:main', 'src', 'pluton')
        self.paths.set_path('package:console', 'package:main', 'cmd')
        self.paths.set_path(
            'package:wwtemplates',
            'package:console',
            'templates',
        )
        self.paths.set_path(
            'package:application',
            'package:main',
            'application',
        )
        self.paths.set_path(
            'package:settings',
            'package:application',
            'settings',
        )
        self.paths.set_path('data', 'cwd', 'data')
        self.paths.set_path('report', 'data', 'report.yml')

        self.paths.set_path('uwsgi:pidfile', 'data', 'uwsgi.pid')
        self.paths.set_path('uwsgi:logto', 'data', 'uwsgi.log')
        self.paths.set_path('uwsgi:daemonize2', 'data', 'uwsgi.daemonize.log')
        self.paths.set_path('uwsgi:socket', 'data', 'uwsgi.socket')

        self.paths.set_path('exe:pytest', 'virtualenv:bin', 'py.test')

    def after_dependencies(self):
        super().after_dependencies()
        self.settings['ignore_inits_dirs'] = self.settings.get(
            'ignore_inits_dirs',
            [],
        )
        self.settings['ignore_inits_dirs'].append('templates')
        self.settings['ignore_inits_dirs'].append('static')
