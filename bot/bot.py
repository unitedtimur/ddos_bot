from vk_api.bot_longpoll import VkBotEventType
from connect import Connect

class Bot:
    def __init__(self):
        self.longpoll = Connect.LONGPOLL
    
    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                print("We have new message!")

if __name__ == '__main__':
    Bot().start()