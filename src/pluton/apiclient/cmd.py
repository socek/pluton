from argparse import ArgumentParser

from pluton.apiclient.client import ApiClient


class Command(object):

    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument(
            '-n',
            '--name',
            dest='name',
            help='Name of the call',
        )

    def run(self):
        self.args = self.parser.parse_args()

        if self.args.name:
            method = getattr(self.client(), self.args.name)
            method(
                'Ermo',
                'normal',
                '{"txt": "This is text", "msg": "This is message"}',
            )
        else:
            self.parser.print_help()

    def client(self):
        api_key = 'bccc31e7-3937-4a67-b546-51a2b0e0ecdd'
        api_secret = 'a7ea6f4b-1cbe-4e3f-870c-359a2a5cf297'
        return ApiClient(api_key, api_secret)


def run():
    Command().run()
