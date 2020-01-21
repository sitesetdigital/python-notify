from .channels.ses import SES


class Publisher(object):

    def __init__(self):
        self.channels = list()
        self.channels.append(SES())

    def publish(self, notice):
        for x in self.channels:
            x.send(notice)
