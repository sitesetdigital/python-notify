from .channels.ses import SES
from .channels.flash import Flash


class Publisher(object):
    """Class to publish notification objects to all channels"""

    def __init__(self):
        self.channels = list()
        self.channels.append(SES())
        self.channels.append(Flash())

    def publish(self, notice):
        """Publish the provided `notice` object to all channels"""
        for x in self.channels:
            x.send(notice)
