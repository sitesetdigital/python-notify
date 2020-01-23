class Email(object):
    """Class to represent an email notification"""

    def __init__(self, to_address: str, subject, *args, **kwargs):
        """
        Create a notification representing an email.

        `to_address` specifies which address to send the email to.

        `to_name` may optionally be specified to include a name along side the `to_address`.

        `subject` may be specified to set the email subject.

        `html_body` and/or `text_body` should be specified to set the email body.

        `reply_to_address` may optionally be specified to set the Reply-To address.

        `reply_to_name` can also be added to compliment the above address.

        `from_address` sets the address that this email is sent from.

        `from_name` can be specified to compliment the above address.
        """
        # TODO: support multiple recipients and cc/bcc
        self.to_address = to_address
        self.to_name = kwargs.get('to_name')
        self.subject = subject
        self.html_body = kwargs.get('html_body')
        self.text_body = kwargs.get('text_body')

        if not self.html_body and not self.text_body:
            raise RuntimeError('No html_body/text_body provided')

        self.reply_to_address = kwargs.get('reply_to_address')
        self.reply_to_name = kwargs.get('reply_to_name')
        self.from_address = kwargs.get('from_address')
        self.from_name = kwargs.get('from_name')