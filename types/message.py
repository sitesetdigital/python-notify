class Message(object):
    
    def __init__(self, message: str, *args, **kwargs):
        self.message = message
        self.category = kwargs.get('category') if kwargs.get('category') else None
