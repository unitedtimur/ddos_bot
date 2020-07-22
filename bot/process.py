from parse_configuration import get_value_by_key, get_values_by_section
from sql import SQL
from api import API

class Process:
    @staticmethod
    def process(user_id, message):
        pass
    
    @staticmethod
    def is_command(message):
        command = message.split()[0].lower()
        commands = get_values_by_section('USER_COMMANDS')
        return command in commands
    
    @staticmethod
    def is_admin_command(user_id, message):
        command = message.split()[0].lower()
        admin_command = get_value_by_key('ADMIN_COMMANDS', 'ADMIN')
        return str(user_id) == '104651526' and command == admin_command

    @staticmethod
    def process_admin_command(user_id, message):
        args = message.split()[1:]
        admin_commands = get_values_by_section('ADMIN_COMMANDS')
        
        if len(args) == 0:
            API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'NO_COMMAND'))
        else:
            print("good")
