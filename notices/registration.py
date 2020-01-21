from .notice import Notice
from ..types.email import Email
from ..types.message import Message


class Registration(Notice):

    def __init__(self, to_email):
        super().__init__()

        self.types.append(
            Email(
                to_email=to_email,
                subject='email subject',
                text_body='this is the plaintext body',
                html_body='this is the html body'
            )
        )

        self.types.append(
            Message('this is a flash message')
        )
