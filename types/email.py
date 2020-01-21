class Email(object):

    def __init__(self, to_email: str, subject, *args, **kwargs):
        self.to_email = to_email
        self.subject = subject
        self.html_body = kwargs.get('html_body')
        self.text_body = kwargs.get('text_body')

        if not self.html_body and not self.text_body:
            raise RuntimeError('No html_body/text_body provided')

        self.reply_to = kwargs.get('reply_to')