from sql.users_table import get_users
from tools.api import messages_send


def notify_bot_started():
    users = get_users()
    if users is not None:
        for admin in filter(lambda user_data: user_data['privilege'] == 'admin', users):
            messages_send(admin['user_id'], 'Bot has been started...')


def notify_bot_stopped():
    users = get_users()
    if users is not None:
        for admin in filter(lambda user_data: user_data['privilege'] == 'admin', users):
            messages_send(admin['user_id'], 'Bot has been stopped...')
