from pluton.apiclient.config import ConfigFile


class Check(object):
    config_file = 'server.yaml'

    def __init__(self, api, arg):
        self.api = api
        self.arg = arg

    def send(self):
        raw = self.check(self.arg)
        self.api.add_event(self.name, 'normal', raw, arg=self.arg)

    def configure(self):
        ConfigFile(self.config_file).add_event(self.name, self.arg)
