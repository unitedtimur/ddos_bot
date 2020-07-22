from vk_api.bot_longpoll import VkBotEventType
from connect import Connect
from process import Process
from log import Log
from parse_configuration import get_value_by_key

class Bot:
    def __init__(self):
        Log.log_info(get_value_by_key('BOT_CONDITION', 'BOT_STARTED'))
        self.longpoll = Connect.LONGPOLL
    
    def __del__(self):
         Log.log_info(take_key_value('BOT_CONDITION', 'BOT_STOPPED'))

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                user_id = event.message.from_id
                message = event.message.text
                isCommand = Process.is_command(message)

                if Process.is_admin_command(user_id, message):
                    Log.log_info(get_value_by_key('REQUESTS', 'ADMIN_REQUEST').format(user_id))
                    Process.process_admin_command(user_id, message)
                elif isCommand:
                    Log.log_info(get_value_by_key('REQUESTS', 'USER_COMMAND_REQUEST').format(user_id))
                else:
                    Log.log_info(get_value_by_key('REQUESTS', 'USER_UNK_COMMAND_REQUEST').format(user_id))


if __name__ == '__main__':
    Bot().start()