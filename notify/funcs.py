from notify.publisher import Publisher


def publish_notification(notification):
    """Publish a notification object"""
    Publisher().publish(notification)