from src import config
from src.permission import *
from src.functionality import *

class ReqProcess:

    def process(self, user_id, message : str):

        #todo запросить статус
        user_permission = Permission('blabla')
        args = message.split()
        target = None
        command_args = {}
        sub_commands = None

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

        size = len(args)
        ok = True
        for i in range(size, 1, 2):
            global size
            global ok

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
