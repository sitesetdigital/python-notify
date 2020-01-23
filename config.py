class Config(object):
    """Config object for package options"""

    def __init__(self, *args, **kwargs):
        """
        `email_from_address` the default 'from' email address.

        `email_from_name` the name to compliment the above address.
        """
        self.email_from_name = None
        self.email_from_address = None