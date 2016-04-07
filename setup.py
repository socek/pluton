# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'pyramid',
    'morfdict>=0.3.7',
    'pyyaml',

    'pyramid_jinja2',
    'pyramid_beaker',
    'formskit',

    'waitress',
    'SQLAlchemy',
    'hamlish_jinja',
    'formskit',

    'fanstatic',
    'js.jquery',
    'js.bootstrap',
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
            'paste.app_factory': (
                'main = pluton.application.app:main',
            )
        }
    )
