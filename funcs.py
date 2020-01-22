from notify.publisher import Publisher


def publish_notification(notification):
    Publisher().publish(notification)