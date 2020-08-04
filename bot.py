from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bot.connect import Connect


class Bot:
    def __init__(self, longpoll: VkBotLongPoll):
        self.longpoll = longpoll

    def listen(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                print("New message!")


Bot(Connect.LONGPOLL).listen()
