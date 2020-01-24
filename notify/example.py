import notify
from notify.notices.registration import Registration
from notify.global_config import global_config
import boto3

from notify.notices.notice import Notice
from notify.types.email import Email
from notify.types.message import Message

# This is our example notification
# of course, this should be kept in a separate file/folder
class MyExampleRegistrationNotice(Notice):

    def __init__(self, to_address):
        super().__init__()

        # This specifies that this notification has an email to send on publication
        self.types.append(
            Email(
                to_address=to_address,
                to_name='to name',
                from_address='localfrom@siteset.digital',
                from_name='local from',
                reply_to_address='replyto@madokami.com',
                reply_to_name='reply to name',
                subject='email subject',
                text_body='this is the plaintext body',
                html_body='this is the html body'
            )
        )

        # Also has a
        self.types.append(
            Message('this is a flash message')
        )


if __name__ == "__main__":
    # Make sure you set up boto3, using env variables in your bootstrapping process
    # boto3.setup_default_session(profile_name='prod')

    # Also set config variables
    global_config.email_from_address = 'test@siteset.digital'
    global_config.email_from_name = 'global from name'

    # Now in our application code...

    # Push our example notification
    notify.publish_notification(MyExampleRegistrationNotice('testing@siteset.co.uk'))