from api.log_listener import setup_log_event_handlers
from api.plan import upgrade_plan
from api.slack_listener import setup_slack_event_handler
from api.user import password_forgotten, register_new_user

setup_log_event_handlers()
setup_slack_event_handler()

# register a new user
register_new_user("Arjan", "BestPasswordEva", "hi@arjanegges.com")

# send a password reset message
password_forgotten("hi@arjanegges.com")

# upgrade the plan
# upgrade_plan("hi@arjanegges.com")
