from vk_api.bot_longpoll import VkBotEventType
from connect import Connect
from process import Process
from log import Log
from parse_configuration import get_value_by_key
from api import API
from threading import Thread

class Bot:
    def __init__(self):
        Log.log_info(get_value_by_key('BOT_CONDITION', 'BOT_STARTED'))
        self.longpoll = Connect.LONGPOLL
    
    def __del__(self):
        Log.log_info(take_key_value('BOT_CONDITION', 'BOT_STOPPED'))

    def process(self, id, msg):
        user_id         = id
        message         = msg
        Process.in_user_table(id)

        if API.groups_isMember(id) == 1:
            if Process.is_admin_command(id, message):
                Process.process_admin_command(user_id, message)
            elif Process.is_command(message):
                Process.process_user_command(user_id, message)
            else:
                API.messages_send(user_id, get_value_by_key('BOT_ANSWER', 'UNKNOWN'))
        else:
            API.messages_send(user_id, get_value_by_key('BOT_ANSWER', 'NOT_SUBSCRIBED').format(user_id))


    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                event_thread = Thread(target = self.process, args = (event.message.from_id, event.message.text))
                event_thread.start()

if __name__ == '__main__':
    Bot().start()