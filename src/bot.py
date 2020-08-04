from src.connect import LONGPOLL
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from src.sql import SQL


class Bot:
    def __init__(self, longpoll: VkBotLongPoll, db: SQL):
        print("Bot has been started...")
        self.longpoll = longpoll
        self.db = db

    def __del__(self):
        print("Bot has been stopped...")

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                print("New message!")


if __name__ == "__main__":
    bot = Bot(LONGPOLL, SQL())
    bot.start()
