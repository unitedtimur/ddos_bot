from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from ddos_bot.processing.request_process import ReqProcess
from ddos_bot.sql.initializing import init_database_connection
from ddos_bot.tools.connect import LONGPOLL


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
                print(f"New message from {event.message.from_id}")


if __name__ == "__main__":
    init_database_connection()
    bot = Bot(LONGPOLL, ReqProcess())
    bot.start()
