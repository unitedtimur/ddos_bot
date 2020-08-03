from parse_configuration import get_value_by_key, get_values_by_section

from sql import SQL
from api import API
from log import Log

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
        level = SQL().find_admin(user_id)
        if level:
            return str(level[0][0]) == 'admin' and command == admin_command
        return False

    @staticmethod
    def is_white(number):
        number = SQL().find_number(number)
        if number: return True
        return False

    @staticmethod
    def process_admin_command(user_id, message):
        args = message.split()[1:]
        admin_commands = get_values_by_section('ADMIN_COMMANDS')
        
        if len(args) == 0:
            API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'NO_COMMAND'))
            return

        # Команда вывода списка пользователей
        if args[0] == get_value_by_key('ADMIN_COMMANDS', 'ADMIN_USER_LIST'):
           rows = SQL().get_rows_from_table(args[1])
           if rows is not None:
               response = "Список пользователей:\n"
               for id, lev in rows: response += 'user_id: ' + str(id) + ' level: ' + str(lev) + '\n'
               API.messages_send(user_id, response)
               Log.log_info(get_value_by_key('LOG', 'GET_USER_LIST').format(user_id))

        # Команда добавления администратора
        elif args[0] == get_value_by_key('ADMIN_COMMANDS', 'ADMIN_ADD_ADMIN'):
            SQL().insert_into_user_table([args[1], 'admin'], 'users')
            API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'ADD_ADMIN'))
            Log.log_info(get_value_by_key('LOG', 'ADD_ADMIN').format(user_id, args[1]))
        
        # Команда удаления администратора
        elif args[0] == get_value_by_key('ADMIN_COMMANDS', 'ADMIN_DEL_ADMIN'):
            SQL().del_admin_from_user_table(args[1])
            API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'DEL_ADMIN'))
            Log.log_info(get_value_by_key('LOG', 'DEL_ADMIN').format(user_id, args[1]))

        # Команда удаления пользователя ИЗ БД (!!!)
        elif args[0] == get_value_by_key('ADMIN_COMMANDS', 'ADMIN_REM_USER'):
            SQL().del_row_from_user_table(args[1])
            API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'REM_ADMIN'))
            Log.log_info(get_value_by_key('LOG', 'REM_ADMIN').format(user_id, args[1]))

        # Команда добавления номера в white list
        elif args[0] == get_value_by_key('ADMIN_COMMANDS', 'ADMIN_ADD_TO_WHITE_LIST'):
            SQL().insert_into_white_list(args[1], args[2])
            API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'ADD_TO_WHITE_LIST').format(args[1], args[2]))

        # Неизвестная ADMIN команда
        else: 
             API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'UNKNOWN'))

    @staticmethod
    def process_user_command(user_id, message):
        msg = message.split()
        command = msg[0].lower()

        # Команда /info
        if command == get_value_by_key('USER_COMMANDS', 'INFO'):
            API.messages_send(user_id, get_value_by_key('USER_RESPONSE', 'INFO'))
        # Команда /ddos
        elif command == get_value_by_key('USER_COMMANDS', 'DDOS'):
            if len(msg) > 3: 
                API.messages_send(user_id, "Введены неверные аргументы!")
                return

            num = msg[1].replace("+7", "")

            if Process.is_white(num):
                API.messages_send(user_id, "На этот номер невозможно произвести атаку!")
                return

            if API.is_already_user_id_ddos(user_id):
                API.messages_send(user_id, get_value_by_key('BOT_ANSWER', 'BOT_USER_ID_ALREADY_DDOS'))
            else:
                API.call_ddos_number(user_id, msg[1], int(msg[2]), int(20))
                API.messages_send(user_id, get_value_by_key('BOT_ANSWER', 'BOT_DDOS').format(msg[1], msg[2], 20))

    @staticmethod
    def in_user_table(user_id):
        SQL().insert_into_users_if_not_exists(user_id)




