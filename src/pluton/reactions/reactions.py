class Reaction(object):
    name = None

    def __init__(self, event):
        self.event = event

    @property
    def raw(self):
        return self.event.raw

    def react(self):
        pass


class PrintEvent(Reaction):
    name = 'print_event'

    def react(self):
        print('React:', self.event.name, self.event.raw)
