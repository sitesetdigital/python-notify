class Message(object):
    """Class to represent a simple message"""

    def __init__(self, message: str, *args, **kwargs):
        """
        Create a notification representing a simple message.

        `message` is the message text to use

        `category` may optionally be specified to categorise the message.
        """
        self.message = message
        self.category = kwargs.get('category') if kwargs.get('category') else None
