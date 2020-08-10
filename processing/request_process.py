from inspect import signature
from time import sleep

from processing.permission import *
from processing.verification import *
from settings.response_info import *
from sql.users_table import get_privilege, get_user, add_user
from tools.api import messages_send, get_fullname_by_user_id
from tools.functionality import call_ddos_number


class ReqProcess:

    def process(self, user_id, message: str):
        # Add user to table if not
        exists_user(user_id)
        # If user is not a group member
        if not is_group_member(user_id):
            messages_send(user_id, info['not_member'])
            return
        # Get the privilege by user_id
        privilege = get_privilege(user_id)
        # Check got privilege
        if not is_privilege(privilege):
            messages_send(user_id, errors['er_privilege'])
            return
        # Split the message like commands
        args = message.lower().strip().split()
        # Processing the commands for user with privilege
        permission_process(user_id, args, privilege)




