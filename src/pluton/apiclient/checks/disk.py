from subprocess import PIPE
from subprocess import Popen

from .base import Check


class DiskCheck(Check):
    name = 'Disk check'

    def check(self, disk):
        spp = Popen(["df", disk], stdout=PIPE)
        output = spp.communicate()[0]
        (
            device,
            size,
            used,
            available,
            percent,
            mountpoint
        ) = output.decode('utf8').split("\n")[1].split()
        return {
            'device': device,
            'size': size,
            'used': used,
            'available': available,
            'percent': percent,
            'mountpoint': mountpoint,
        }
