from .channel import Channel
from ..notices.notice import Notice
from ..types.email import Email
from ..global_config import global_config
import boto3


class SES(Channel):

    def send(self, notice: Notice):
        for n in notice.types:
            if isinstance(n, Email):
                self._send_email(n)

    def _send_email(self, email: Email):
        ses = boto3.client('ses')
        result = ses.send_email(
            Source=self._format_name_address(email.from_name, email.from_address) if email.from_address else
            self._format_name_address(global_config.email_from_name, global_config.email_from_address),
            Destination={
                'ToAddresses': [
                    self._format_name_address(email.to_name, email.to_address)
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
            ReplyToAddresses=[ self._format_name_address(email.reply_to_name, email.reply_to_address) ] if email.reply_to_address else []
        )

        return result

    def _format_name_address(self, name, address) -> str:
        return '%s <%s>' % (name, address) if name else address

    def _create_body(self, email: Email) -> dict:
        body = {}

        if email.text_body:
            body['Text'] = {'Data': email.text_body}

        if email.html_body:
            body['Html'] = {'Data': email.html_body}

        return body
