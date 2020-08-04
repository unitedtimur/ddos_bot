import random

from vk_api import vk_api

from src import connect

API = connect.VK

def get_random_id():
    # Вычисляем random_id для предотвращения повторных отправок сообщения
    return random.getrandbits(31) * random.choice([-1, 1])

def get_fullname_by_user_id(user_id):
    try:
        response = API.method('users.get', { 'user_ids': user_id })[0]
    except Exception:
        return 'unknown'
    return response["first_name"] + ' ' + response['last_name']