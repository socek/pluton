def make_settings(settings, paths):
    database(settings, paths)


def database(settings, paths):
    settings['db']['type'] = 'postgresql'
    settings['db']['login'] = 'pluton'
    settings['db']['password'] = 'plutonexec'
    settings['db']['host'] = 'localhost'
    settings['db']['port'] = '5432'
    settings['db']['name'] = '%(project)s_tests'
