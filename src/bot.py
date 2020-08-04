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
                self.process.process(event.message.from_id, event.message.text)


if __name__ == "__main__":
    bot = Bot(LONGPOLL, Process())
    bot.start()
