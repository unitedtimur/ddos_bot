from processing.permission import *
from processing.verification import *
from settings.response_info import *
from sql.users_table import get_privilege
from tools.api import messages_send

import settings.config as config
from inspect import signature


class ReqProcess:

    def __process_ddos_call(self, user_id, number: str, time: int = None, stop: bool = False):
        print(user_id, number, time, stop)

    def __process_bl_call(self, user_id, number: str, command: str):
        pass

    def __process_info_call(self, user_id, command: str = 'h'):
        pass

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
        #permission_process(user_id, args, privilege)

        privilege = get_privilege(user_id)

        args = message.lower().strip().split()
        target = None
        commands_config = config.commands_config[privilege]
        command_args = {}
        size = len(args)
        error_code = 0

        try:
            if args[0] in commands_config:
                general_command = args[0]
                command_config = commands_config[general_command]
                sub_commands = command_config[0]
                day_limit = command_config[1]

                if general_command == '/ddos':
                    target = self.__process_ddos_call
                elif general_command == '/bl':
                    target = self.__process_bl_call
                else:
                    target = self.__process_info_call
            else:
                raise ValueError(user_id, error_code)

            it = iter(range(1, size))
            for i in it:
                if args[i] in sub_commands:
                    subcommand_info = sub_commands[args[i]]

                    if subcommand_info['anum'] == 1:
                        i = next(it)
                        if i < size:

                            arg = subcommand_info['atype'](args[i])
                            arg_limit = subcommand_info['lim']

                            if arg_limit >= 0 and (arg < 0 or arg > arg_limit):
                                raise ValueError(user_id, error_code)

                            command_args[subcommand_info['name']] = arg
                        else:
                            error_code = 2
                            raise ValueError(user_id, error_code)
                    else:
                        command_args[subcommand_info['name']] = args[i]
                else:
                    raise ValueError(user_id, error_code)

            parameters = signature(target).parameters
            if len(command_args) > len(parameters):
                raise ValueError(user_id, error_code)

            for value in list(parameters.values())[1:]:
                if value.default is value.empty and value.name not in command_args:
                    raise ValueError(user_id, error_code)

            target(user_id, **command_args)

        except ValueError as err:
            msg = None
            if len(err.args) == 1 or err.args[1] == 0:
                msg = "Неверно переданы аргументы. Попробуйте снова."
            elif err.args[1] == 1:
                msg = "Превышены допустимые ограничения. Попробуйте снова."
            elif err.args[1] == 2:
                msg = "Не предоставлены все аргументы переданных команд. Попробуйте снова."
            elif err.args[1] == 3:
                msg = "Не переданны необходимые команды. Попробуйте снова."
            messages_send(err.args[0], msg)
