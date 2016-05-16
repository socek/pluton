from .command import PlutonCommand
from .command import PlutonSingleCommand
from .develop import RunTests


def run():
    PlutonCommand().run()


def runtest():
    PlutonSingleCommand(RunTests).run()
