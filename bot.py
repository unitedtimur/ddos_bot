import threading

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from processing.request_process import ReqProcess
from sql.initializing import init_database_connection
from tools.connect import LONGPOLL
from tools.functionality import call_ddos_number, stop_ddos_number, ddos_dict


class Bot:
    def __init__(self, longpoll: VkBotLongPoll, process: ReqProcess):
        print("Bot has been started...")
        self.longpoll = longpoll
        self.process = process

    def __del__(self):
        print("Bot has been stopped...")

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.process.process(event.message.from_id, event.message.text)

if __name__ == "__main__":
    init_database_connection()
    bot = Bot(LONGPOLL, ReqProcess())
    bot.start()
