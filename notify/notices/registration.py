from .notice import Notice
from ..types.email import Email
from ..types.message import Message


class Registration(Notice):

    def __init__(self, to_address):
        super().__init__()

        self.types.append(
            Email(
                to_address=to_address,
                to_name='to name',
                from_address='localfrom@siteset.digital',
                from_name='local from',
                reply_to_address='replyto@madokami.com',
                reply_to_name='reply to name',
                subject='email subject',
                text_body='this is the plaintext body',
                html_body='this is the html body'
            )
        )

        self.types.append(
            Message('this is a flash message')
        )
