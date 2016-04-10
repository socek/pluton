def make_settings(settings, paths):
    database(settings, paths)
    settings['threads'] = 1


def database(settings, paths):
    # ----------------------------------------
    # This is example postgresql configuration
    # ----------------------------------------
    settings['db']['type'] = 'postgresql'
    settings['db']['login'] = 'pluton'
    settings['db']['password'] = 'plutonexec'
    settings['db']['host'] = 'localhost'
    settings['db']['name'] = 'pluton'
    settings['db']['port'] = '5432'
    print(settings['db']['url'])
