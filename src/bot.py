from src.api import get_fullname_by_user_id
from src.connect import LONGPOLL
from src.process import Process
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class Bot:
    def __init__(self, longpoll: VkBotLongPoll, process: Process):
        print("Bot has been started...")
        self.longpoll = longpoll
        self.process = process

    def __del__(self):
        print("Bot has been stopped...")

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                pass
                #self.process.process(event.message.from_id, event.message.text)



from src.sql.operations import *

if __name__ == "__main__":
    init_database_connection()
    print(get_user(1))
    bot = Bot(LONGPOLL, Process())
    bot.start()

