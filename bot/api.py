import random
from connect import Connect

class API:
    api = Connect.VK

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