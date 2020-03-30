class Attachment(object):
    """Class to represent an Attachment for emails"""

    def __init__(self, *args, **kwargs):
        """
        Create an Attachment to include within an email.

        `file` specify the file to attach to an email.

        `name` specifies the name of the attachment within an email.
        
        `type` specifies the filetype of the attachment file.
        """
        self.file = kwargs.get('file')
        self.name = kwargs.get('name')
        self.type = kwargs.get('type')
