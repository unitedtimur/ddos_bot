from time import sleep

from processing.permission import *
from processing.verification import *
from settings.response_info import *
from sql.users_table import get_privilege, get_user, add_user
from tools.api import messages_send, get_fullname_by_user_id
from tools.functionality import call_ddos_number, process_bl, send_info


class ReqProcess:

    def process(self, user_id, message : str, call_ddos_number=None):
        # Add user to table if not
        exists_user(user_id)
        # If user is not a group member
        if not is_group_member(user_id):
            messages_send(user_id, info('not_member'))
            return
        # Get the privilege by user_id
        privilege = get_privilege(user_id)
        # Check geted privilege
        if not is_privilege(privilege):
            messages_send(user_id, errors['er_privilege'])
            return
        # Get something...
        user_permission = Permission(privilege)
        # Parse the message by command
        args = message.lower().strip().split()


        target = None
        command_args = {}

        if args[0] in user_permission.available_commands:
            general_command = args[0]
            sub_commands = user_permission.available_commands[general_command]

            if general_command == '/ddos':
                target = call_ddos_number
                command_args = {
                    'time'   : (config.standard_limits['dtime']),
                    'threads': (config.standard_limits['th'])
                }
            elif general_command == '/bl':
                target = process_bl
            else:
                target = send_info
                command_args = {
                    'command' : '-h'
                }
        else:
            messages_send(user_id, errors['er_invalid_args'])
            return

        size = len(args)
        ok = True
        error_code = 0

        it = iter(range(1, size))
        for i in it:
            if args[i] in sub_commands:

                command_info = sub_commands[args[i]]

                if command_info[1] == 1:
                    i = next(it)

                    if i < size:
                        if command_info[2] > 0:
                            try:
                                arg = int(args[i])
                                if 0 < arg <= command_info[2]:
                                    command_args[command_info[0]] = arg
                                else:
                                    ok = False
                                    error_code = 1
                                    break
                            except Exception:
                                ok = False
                                break
                        else:
                            command_args[command_info[0]] = args[i]
                    else:
                        ok = False
                        error_code = 2
                        break
                else:
                    command_args[command_info[0]] = args[i]
            else:
                ok = False
                break

        if ok:
            if len(signature(target).parameters) != len(command_args) + 1:
                ok = False
                error_code = 3

        if not ok:
            msg = None
            if error_code == 0:
                msg = "Неверно переданы аргументы. Попробуйте снова."
            elif error_code == 1:
                msg = "Превышены допустимые ограничения. Попробуйте снова."
            elif error_code == 2:
                msg = "Не предоставлены все аргументы переданных команд. Попробуйте снова."
            elif error_code == 3:
                msg = "Не переданны необходимые команды. Попробуйте снова."
            messages_send(user_id, msg)
            return

        target(user_id, **command_args)
