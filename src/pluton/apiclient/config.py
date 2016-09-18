from os.path import exists

from yaml import dump
from yaml import load


class ConfigFile(object):

    def __init__(self, path):
        self.path = path
        self.data = {
            'events': [],
        }

    def read_yaml(self):
        if exists(self.path):
            with open(self.path, 'r') as stream:
                self.data = load(stream)

    def write_yaml(self):
        with open(self.path, 'w') as stream:
            self.data = dump(
                self.data,
                stream,
                default_flow_style=False,
            )

    def add_event(self, name, arg=None):
        self.read_yaml()

        data = {
            'name': name,
            'arg': arg,
        }
        if data not in self.data['events']:
            self.data['events'].append(data)

            self.write_yaml()
