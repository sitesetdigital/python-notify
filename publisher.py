from .channels.ses import SES
from .channels.flash import Flash


class Publisher(object):

    def __init__(self):
        self.channels = list()
        self.channels.append(SES())
        self.channels.append(Flash())

    def publish(self, notice):
        for x in self.channels:
            x.send(notice)
