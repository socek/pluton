from subprocess import PIPE
from subprocess import Popen


def disk_space_check(disk):
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
