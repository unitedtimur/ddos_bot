from sql.users_table import get_users, get_privilege
from tools.api import messages_send


def bot_started():
    for admin in get_users():
        if get_privilege(admin.split()[0]) == 'admin':
            messages_send(admin.split()[0], 'Bot has been started...')

def bot_stopped():
    for admin in get_users():
        if get_privilege(admin.split()[0]) == 'admin':
            messages_send(admin.split()[0], 'Bot has been stopped...')