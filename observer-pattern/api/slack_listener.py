from lib.slack import post_slack_message

from .event import subscribe


def handle_user_registered_event(user):
    post_slack_message("sales", f"{user.name} has registered with email address {user.email}. Don't forget to spam this user")
    
def setup_slack_event_handler():
    subscribe("user_registered_event", handle_user_registered_event)
    