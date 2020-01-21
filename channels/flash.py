from .channel import Channel
from ..notices.notice import Notice
from ..types.message import Message


class Flash(Channel):

    def send(self, notice: Notice):
        for n in notice.types:
            if isinstance(n, Message):
                self._flash_message(n)

    def _flash_message(self, message: Message):
        # TODO: support other web frameworks
        from flask import flash
        flash(message.message, message.category if message.category is not None else "message")
