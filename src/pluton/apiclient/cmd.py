from argparse import ArgumentParser

from pluton.apiclient.client import ApiClient
from pluton.apiclient.checks.disk import DiskCheck


class Command(object):

    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument(
            '-n',
            '--name',
            dest='name',
            help='Name of the call',
        )

        self.parser.add_argument(
            '-d',
            '--disk',
            dest='disk',
            help='Send disk data',
        )

        self.parser.add_argument(
            '-c',
            '--config',
            dest='config',
            help='Create config file for server',
            action='store_true',
        )

    def get_check(self):
        if self.args.disk:
            return DiskCheck(self.client(), self.args.disk)

    def run(self):
        self.args = self.parser.parse_args()
        check = self.get_check()

        if self.args.name:
            method = getattr(self.client(), self.args.name)
            method(
                'Ermo',
                'normal',
                '{"txt": "This is text", "msg": "This is message"}',
            )
        elif self.args.config and check:
            print("Saving check config...")
            check.configure()
        elif check:
            print("Sending check...")
            check.send()
        else:
            self.parser.print_help()

    def client(self):
        api_key = 'bccc31e7-3937-4a67-b546-51a2b0e0ecdd'
        api_secret = 'a7ea6f4b-1cbe-4e3f-870c-359a2a5cf297'
        return ApiClient(api_key, api_secret)


def run():
    Command().run()
