from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from processing.request_process import ReqProcess
from sql.initializing import init_database_connection
from tools.admin_panel import bot_started, bot_stopped
from tools.connect import LONGPOLL


class Bot:
    def __init__(self, longpoll: VkBotLongPoll, process: ReqProcess):
        bot_started()
        self.longpoll = longpoll
        self.process = process

    def __del__(self):
        bot_stopped()

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.process.process(event.message.from_id, event.message.text)


if __name__ == "__main__":
    init_database_connection()
    bot = Bot(LONGPOLL, ReqProcess())
    bot.start()
