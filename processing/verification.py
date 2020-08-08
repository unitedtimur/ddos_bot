from ddos_bot.sql.users_table import get_user, add_user
from ddos_bot.tools.api import *


def is_group_member(user_id) -> bool:
    if API.method('groups.isMember', {'group_id': POLL.group_id, 'user_id': user_id}) == 1:
        return True
    return False


def exists_user(user_id) -> None:
    if get_user(user_id) is None:
        name, surname = get_fullname_by_user_id(user_id)
        add_user(user_id, name, surname, 'user')
