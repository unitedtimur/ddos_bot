from threading import Thread

from settings.config import available_commands
from settings.response_info import info, errors, priv_info
from sql.blacklist_table import get_number, add_number, rem_number
from sql.ddosnumberlist_table import add_number as add_number_to_history
from tools.api import info_keyboard, messages_send_key, messages_send
from tools.functionality import parse_number, get_ddos_numbers_by_user_id, call_ddos_number, stop_ddos_number, ddos_dict


def permission_process(user_id: str, args: list, privilege: str) -> None:
    if args[0] == '/info':
        limit = available_commands[privilege]
        messages_send(user_id, priv_info['general']['ddos'].format(limit['ddos']['time'], limit['ddos']['count']))
        if privilege != 'user':
            messages_send(user_id, priv_info['not_jeneral']['bl'])
        return

    if args[0] == '/ddos':
        ddos(user_id, args, privilege)
    elif args[0] == '/bl':
        bl(user_id, args, privilege)
    else:
        messages_send_key(user_id, errors['er_not_command'], info_keyboard())


def ddos(user_id: str, args: list, privilege: str):
    if len(args) == 3:
        if args[1] == 'stop':
            pr_number = parse_number(args[2])
            if pr_number is not None:
                stop_ddos_number(user_id, pr_number)
            else:
                messages_send_key(user_id, errors['er_stop_ddos'], info_keyboard())
            return

    if len(args) == 2:
        if args[1] == 'ls':
            list_ddos_numbers = []
            if user_id in ddos_dict:
                for num in ddos_dict[user_id]:
                    list_ddos_numbers.append('+' + str(num))
                messages_send(user_id, info['ddos_list_now'].format('\n'.join(list_ddos_numbers)))
                return
            else:
                messages_send_key(user_id, errors['er_no_ddos_numbers'], info_keyboard())
                return

    if len(args) != 3:
        messages_send_key(user_id, errors['er_invalid_args'].format(args[0]), info_keyboard())
        return

    num = parse_number(args[1])
    if num is None:
        messages_send_key(user_id, errors['er_invalid_number'], info_keyboard())
        return

    time = int(args[2])
    limits = available_commands[privilege]['ddos']
    if time > limits['time']:
        messages_send_key(user_id, errors['er_no_priv_args'].format(limits['time']), info_keyboard())
        return

    ddos_numbers = get_ddos_numbers_by_user_id(user_id)
    if ddos_numbers is not None:
        print(len(ddos_numbers))
        if len(ddos_numbers) >= limits['count']:
            messages_send_key(user_id, errors['er_limit_ddos_num'].format('\n'.join(ddos_numbers.keys())),
                              info_keyboard())
            return

    if ddos_numbers is not None:
        if num in ddos_numbers.keys():
            messages_send_key(user_id, errors['er_already_ddos'].format(num), info_keyboard())
            return

    add_number_to_history(user_id, num)
    Thread(target=call_ddos_number, args=(user_id, num, time, 15)).start()


def bl(user_id: str, args: list, privilege: str):
    if len(args) > 3:
        messages_send_key(user_id, errors['er_invalid_args'].format(args[0]), info_keyboard())
        return

    if privilege == 'user':
        messages_send_key(user_id, errors['er_no_access'], info_keyboard())
        return

    limits = available_commands[privilege]['bl']
    if args[1] not in limits:
        messages_send_key(user_id, errors['er_invalid_args'].format(args[0]), info_keyboard())
        return

    if args[1] == 'add':
        num = parse_number(args[2])
        if num is None:
            messages_send_key(user_id, errors['er_invalid_number'], info_keyboard())
            return

        numbers = get_number(user_id)
        if len(numbers) >= limits['add']:
            messages_send_key(user_id, errors['er_limit_bl_num'], info_keyboard())
            return

        for n in numbers:
            if num in n.split()[1]:
                messages_send_key(user_id, errors['er_already_in_table'].format(num), info_keyboard())
                return

        add_number(user_id, num)
        messages_send(user_id, info['bl_add'].format(num))
        return

    if args[1] == 'rem':
        num = parse_number(args[2])
        if num is None:
            messages_send_key(user_id, errors['er_invalid_number'], info_keyboard())
            return

        if not rem_number(user_id, num):
            messages_send_key(user_id, errors['er_no_rem'], info_keyboard())
            return

        messages_send(user_id, info['bl_rem'].format(num))
        return

    if args[1] == 'ls':
        numbers = get_number(user_id)

        if len(numbers) == 0:
            messages_send_key(user_id, errors['er_no_numbers'], info_keyboard())
            return

        res = ""
        index = 0
        for n in numbers:
            index += 1
            res += (f'{index}: +' + n.split()[1] + '\n')
        messages_send(user_id, info['bl_ls'].format(res))
        return
