from .channel import Channel
from ..notices.notice import Notice
from ..types.message import Message
from flask import flash


class Flash(Channel):

    def send(self, notice: Notice):
        for n in notice.types:
            if isinstance(n, Message):
                self._flash_message(n)

    def _flash_message(self, message: Message):
        flash(message.message, message.category)
