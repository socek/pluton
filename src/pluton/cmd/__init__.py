from .command import PlutonCommand
from .command import PlutonSingleCommand
from .develop import RunCoverage
from .develop import RunTests


def run():
    PlutonCommand().run()


def runtest():
    PlutonSingleCommand(RunTests).run()


def runcoverage():
    PlutonSingleCommand(RunCoverage).run()
