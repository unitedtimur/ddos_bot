import random

from tools import connect
from tools.connect import LONGPOLL
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

API = connect.VK
POLL = LONGPOLL


def info_keyboard() -> VkKeyboard:
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button(label='/info', color=VkKeyboardColor.POSITIVE)
    return keyboard.get_keyboard()


def get_random_id():
    # Вычисляем random_id для предотвращения повторных отправок сообщения
    return random.getrandbits(31) * random.choice([-1, 1])


def get_fullname_by_user_id(user_id) -> tuple:
    try:
        response = API.method('users.get', {'user_ids': user_id})[0]
        return (response["first_name"], response['last_name'])
    except Exception:
        return ('unknown',)


def messages_send(user_id, message) -> None:
    API.method('messages.send', {
        'user_id': user_id,
        'random_id': get_random_id(),
        'message': message
    })


def messages_send_key(user_id, message, keyboard) -> None:
    API.method('messages.send', {
        'user_id': user_id,
        'random_id': get_random_id(),
        'message': message,
        'keyboard': keyboard
    })
