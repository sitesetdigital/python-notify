from .channel import Channel
from ..notices.notice import Notice
from ..types.email import Email

import boto3


class SES(Channel):

    def __init__(self):
        self.from_email = 'test@siteset.digital'

    def send(self, notice: Notice):
        for n in notice.types:
            if isinstance(n, Email):
                self._send_email(n)

    def _send_email(self, email: Email):
        ses = boto3.client('ses')
        result = ses.send_email(
            Source=self.from_email,
            Destination={
                'ToAddresses': [
                    email.to_email
                ],
                'CcAddresses': [

                ],
                'BccAddresses': [

                ]
            },
            Message={
                'Subject': {
                    'Data': email.subject
                },
                'Body': self._create_body(email)
            },
            ReplyToAddresses=[ email.reply_to ] if email.reply_to else []
        )

        return result

    def _create_body(self, email: Email) -> dict:
        body = {}

        if email.text_body:
            body['Text'] = {'Data': email.text_body}

        if email.html_body:
            body['Html'] = {'Data': email.html_body}

        return body
