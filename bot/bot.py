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
        user_id     = id
        message     = msg
        isCommand   = Process.is_command(message)
        isAdmin     = Process.is_admin_command(id, message)
        isMember    = API.groups_isMember(id)
        
        Process.in_user_table(id)

        if isMember== 1:
            if isAdmin:
                Log.log_info(get_value_by_key('REQUESTS', 'ADMIN_REQUEST').format(id))
                admin_process_thread = Thread(target =  Process.process_admin_command, args = (id, message))
                admin_process_thread.start()
            elif isCommand:
                Log.log_info(get_value_by_key('REQUESTS', 'USER_COMMAND_REQUEST').format(id))
            else:
                API.messages_send(id, get_value_by_key('BOT_ANSWER', 'UNKNOWN'))
                Log.log_info(get_value_by_key('REQUESTS', 'USER_UNK_COMMAND_REQUEST').format(id))
        else:
            API.messages_send(id, get_value_by_key('BOT_ANSWER', 'NOT_SUBSCRIBED'))
            Log.log_info(get_value_by_key('REQUESTS', 'NOT_SUBSCRIBED'))


    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                event_thread = Thread(target = self.process, args = (event.message.from_id, event.message.text))
                event_thread.start()

if __name__ == '__main__':
    Bot().start()