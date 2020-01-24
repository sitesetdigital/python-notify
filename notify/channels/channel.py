from ..notices.notice import Notice
from ..types.email import Email


class Channel(object):
    """Base class which all channel implementations should extend"""

    def send(self, notice: Notice):
        """Send a notice through the channel. Must be implemented in subclasses"""
        raise NotImplementedError()
