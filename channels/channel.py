from ..notices.notice import Notice
from ..types.email import Email


class Channel(object):

    def send(self, notice: Notice):
        raise NotImplementedError()
