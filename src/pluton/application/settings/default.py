def make_settings(settings, paths):
    project(settings, paths)
    session(settings, paths)
    database(settings, paths)
    fanstatic(settings, paths)
    logger(settings, paths)
    debug(settings, paths)


def session(settings, paths):
    settings['session.type'] = 'file'
    settings['session.key'] = 'needtochangethis'
    settings['session.secret'] = 'needtochangethistoo'
    settings['session.cookie_on_exception'] = True

    paths['session'] = {
        'data_dir': ["%(data)s", 'sessions', 'data'],
        'lock_dir': ["%(data)s", 'sessions', 'lock'],
    }
    settings['session.data_dir'] = '%(paths:session:data_dir)s'
    settings['session.lock_dir'] = '%(paths:session:lock_dir)s'


def database(settings, paths):
    # ----------------------------------------
    # This is example postgresql configuration
    # ----------------------------------------
    # settings['db']['type'] = 'postgresql'
    # settings['db']['login'] = 'develop'
    # settings['db']['password'] = 'develop'
    # settings['db']['host'] = 'localhost'
    # settings['db']['port'] = '5432'
    settings['db']['type'] = 'sqlite'
    settings['db']['name'] = '%(project)s_develop'
    paths.set_path('sqlite_db', 'data', '%(db:name)s.db')
    paths['db'] = settings['db']


def project(settings, paths):
    paths.set_path('maindir', 'project', '../..')
    paths.set_path('data', 'maindir', 'data')
    paths.set_path('frontend', 'data', 'frontend.ini')

    paths.set_path('application', 'project', 'application')
    paths.set_path('routing', 'application', 'routing.yaml')


# def alembic(settings, paths):
#     paths['alembic'] = {
#         'versions': ["%(maindir)s", 'migrations'],
#         'ini': ["%(data)s", "alembic.ini"],
#     }


def debug(settings, paths):
    settings['debug'] = True
    settings['pyramid.reload_templates'] = True
    settings['pyramid.debug_notfound'] = True
    settings['pyramid.debug_routematch'] = True


def fanstatic(settings, paths):
    settings['fanstatic'] = {
        'bottom': True,
        'debug': True,
    }


def logger(settings, paths):
    settings['loggers'] = {
        'loggers': {
            'keys': 'root, sqlalchemy, alembic',
        },
        'handlers': {
            'keys': 'console, all',
        },
        'formatters': {
            'keys': 'generic',
        },
        'logger_root': {
            'level': 'INFO',
            'handlers': 'console, all',
        },
        'logger_sqlalchemy': {
            'level': 'INFO',
            'handlers': 'all',
            'qualname': 'sqlalchemy.engine',
            'propagate': '0',
        },
        'logger_alembic': {
            'level': 'INFO',
            'handlers': 'all',
            'qualname': 'alembic',
            'propagate': '0',
        },
        'handler_console': {
            'class': 'StreamHandler',
            'args': '(sys.stderr,)',
            'level': 'NOTSET',
            'formatter': 'generic',
        },
        'handler_all': {
            'class': 'FileHandler',
            'args': "('%%(log_all)s', 'a')",
            'level': 'NOTSET',
            'formatter': 'generic',
        },
        'formatter_generic': {
            'format': '%%(asctime)s %%(levelname)-5.5s [%%(name)s][%%(threadName)s] %%(message)s',
        },
    }
