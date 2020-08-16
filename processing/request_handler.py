from processing.verification import *
from sql.ddosnumberlist_table import *
from inspect import signature
from datetime import datetime
from processing.commands import *
from itertools import chain


class ReqHandler:

    def handle(self, user_id, message: str):

        add_user_if_not_exists(user_id)
        user_pas = Passport(user_id)

        # If user is not a group member
        if not is_group_member(user_pas.user_id):
            messages_send(user_pas.user_id, info['not_member'])
            return
        # Check got privilege
        if not is_privilege(user_pas.privilege):
            messages_send(user_pas.user_id, errors['er_privilege'])
            return

        self.__parse_args(user_pas, message)

    def __parse_args(self, user_pas: Passport, message: str):
        args = message.lower().strip().split()
        command = None
        command_args = {'user_pas': user_pas}

        if args[0] not in user_pas.commands_config:
            messages_send(user_pas.user_id, errors['er_not_command'])
            return

        general_command = args[0]

        if general_command == '/help':
            help_command(user_pas)
            return

        command_config = user_pas.commands_config[general_command]
        sub_commands = command_config['param']
        limits = command_config['lim']

        current_date = datetime.today().strftime('%Y-%m-%d')
        if 'daylim' in limits:
            if limits['daylim'] < len(get_committed_attacks(user_pas.user_id, current_date)):
                messages_send(user_pas.user_id, errors['er_daylim'])
                return

        if 'simult' in limits and user_pas.user_id in ddos_dict:
            if limits['simult'] < len(ddos_dict[user_pas.user_id]):
                messages_send(user_pas.user_id, errors['er_simult_attacks'])
                return

        if general_command == '/ddos':
            command = ddos_command
        elif general_command == '/bl':
            command = blist_command
        else:
            command = set_command

        try:

            size = len(args)
            i = 1
            while i < size:
                if args[i] in sub_commands:
                    subcommand_info = sub_commands[args[i]]

                    if subcommand_info['argnum'] == 1:
                        i += 1
                        if i < size:
                            arg = subcommand_info['argtype'](args[i])

                            if 'lim' in subcommand_info:
                                arg_lim = subcommand_info['lim']
                                if arg < 0 or arg > arg_lim:
                                    messages_send(user_pas.user_id, errors['er_time_lim'].format(str(arg_lim)))
                                    return

                            command_args[subcommand_info['name']] = arg
                        else:
                            messages_send(user_pas.user_id, errors['er_invalid_args'].format(
                                    general_command,
                                    general_command))
                            return
                    else:
                        command_args[subcommand_info['name']] = subcommand_info['default']

                        if 'next_param' in subcommand_info:
                            args.insert(i + 1, subcommand_info['next_param'])
                            size += 1
                else:
                    messages_send(user_pas.user_id, errors['er_invalid_args'].format(
                            general_command,
                            general_command))
                    return
                i += 1

            if len(command_args) > len(signature(command).parameters):
                messages_send(user_pas.user_id, errors['er_invalid_args'].format(
                        general_command,
                        general_command))
                return

            command(**command_args)

        except ValueError:
            messages_send(user_pas.user_id, errors['er_invalid_args'].format(
                    general_command,
                    general_command))
