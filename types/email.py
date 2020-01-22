from ..global_config import global_config


class Email(object):

    def __init__(self, to_address: str, subject, *args, **kwargs):
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