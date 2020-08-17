from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from sql.initializing import init_database_connection
from processing.request_handler import ReqHandler
from tools.connect import LONGPOLL
from tools.admin_panel import *


class Bot:
    def __init__(self, longpoll: VkBotLongPoll, handler: ReqHandler):
        notify_bot_started()
        self.longpoll = longpoll
        self.handler = handler

    def __del__(self):
        notify_bot_stopped()

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.handler.handle(event.message.from_id, event.message.text)


if __name__ == "__main__":
    init_database_connection()
    bot = Bot(LONGPOLL, ReqHandler())
    bot.start()
