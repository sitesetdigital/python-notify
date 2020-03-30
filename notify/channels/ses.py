from .channel import Channel
from ..notices.notice import Notice
from ..types.email import Email
from ..global_config import global_config
import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class SES(Channel):
    """Class for sending notifications via AWS SES"""

    def send(self, notice: Notice):
        """
        Send notice through flash channel. This channel handles notices of `notify.types.email.Email`
        """
        for n in notice.types:
            if isinstance(n, Email):
                self.send_email(n)

    def send_email(self, email: Email, client = None):
        """Send the given notice as an SES email"""

        if client is None:
            client = boto3.client('ses')

        msg = MIMEMultipart()

        msg["Subject"] = email.subject
        msg["To"] = self._format_name_address(email.to_name, email.to_address)
        msg["Cc"] = ''
        msg["Bcc"] = ''
        msg['reply-to'] = self._format_name_address(email.reply_to_name, email.reply_to_address)

        if email.text_body:
            msg.attach(
                MIMEText(email.text_body, 'plain')
            )
        
        if email.html_body:
            msg.attach(
                MIMEText(email.html_body, 'html')
            )
        
        for attachment in email.attachments:
            msg.attach(
                MIMEApplication(
                    attachment.file,
                    Name = attachment.name
                )
            )

        result = client.send_raw_email(
            Source=self._format_name_address(email.from_name, email.from_address) if email.from_address else
            self._format_name_address(global_config.email_from_name, global_config.email_from_address),
            RawMessage={
                'Data': msg.as_string()
            },
        )

        return result

    def _format_name_address(self, name, address) -> str:
        """
        Format a given email address (and optionally a name)
        e.g Jane Doe <jane.doe@example.com>
        """
        return '%s <%s>' % (name, address) if name else address
