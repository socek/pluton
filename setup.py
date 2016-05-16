# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'pyramid',
    'morfdict>=0.3.7',
    'pyyaml',
    'pyramid_ipython',

    'pyramid_jinja2',
    'pyramid_beaker',
    'formskit',

    'waitress',
    'hamlish_jinja',
    'formskit',

    'SQLAlchemy',
    'alembic',
    'psycopg2',

    'fanstatic',
    'js.jquery',
    'js.bootstrap',
    'requests',

    'bael.project==0.2.3',
    'baelfire==0.3.2',
    'uwsgi',
    'pytest',
]


if __name__ == '__main__':
    setup(
        name='pluton',
        version='0.1',
        description='Pluton',
        url='https://github.com/socek/pluton',
        license='Apache License 2.0',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=install_requires,
        entry_points={
            'fanstatic.libraries': (
                'main = pluton.application.resources:library',
            ),
            'paste.app_factory': (
                'main = pluton.application.app:main',
            ),
            'console_scripts': (
                'pclient = pluton.apiclient.cmd:run',
                'pcmd = pluton.cmd:run',
                'ptest = pluton.cmd:runtest',
            ),
        }
    )
