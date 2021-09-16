from lib.log import log
from lib.slack import post_slack_message

from .event import subscribe


def handle_user_registered_event(user):
    print('test')
    log(f"{user.name} has registered with email address {user.email}.")

def handle_user_password_forgotten_event(user):
    log(f"{user.name} has registered with email address {user.email}.")
    
def setup_log_event_handlers():
    subscribe("user_registered_event", handle_user_registered_event)
    subscribe("user_password_forgotten_event", handle_user_password_forgotten_event)
