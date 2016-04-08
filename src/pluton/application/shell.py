from pluton.application.app import main
from pluton.application.controller import PluggedController


def setup(env):
    env['main'] = main
    env['controller'] = PluggedController(env['root_factory'], env['request'])
    env['db'] = env['controller'].database()
