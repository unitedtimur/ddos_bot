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
    def process_admin_command(user_id, message):
        args = message.split()[1:]
        admin_commands = get_values_by_section('ADMIN_COMMANDS')
        
        if len(args) == 0:
            API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'NO_COMMAND'))
            return

        # Команда вывода списка пользователей
        if args[0] == get_value_by_key('ADMIN_COMMANDS', 'ADMIN_USER_LIST'):
            try:
                rows = SQL().get_rows_from_table('users', args[1])
                if rows is not None:
                    response = "Список пользователей:\n"
                    for id, lev in rows: response += 'user_id: ' + str(id) + ' level: ' + str(lev) + '\n'
                    API.messages_send(user_id, response)
                    Log.log_info(get_value_by_key('LOG', 'GET_USER_LIST').format(user_id))
                else:
                    Log.log_crit(get_value_by_key('ERROR', 'ADMIN_USER_LIST'))
            except Exception as e:
                Log.log_crit(e)

        # Команда добавления администратора
        elif args[0] == get_value_by_key('ADMIN_COMMANDS', 'ADMIN_ADD_ADMIN'):
            try:
                SQL().insert_into_user_table([args[1], 'admin'], 'users')
                API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'ADD_ADMIN'))
                Log.log_info(get_value_by_key('LOG', 'ADD_ADMIN').format(user_id, args[1]))
            except Exception as e:
                Log.log_crit(e)
        
        # Команда удаления администратора
        elif args[0] == get_value_by_key('ADMIN_COMMANDS', 'ADMIN_DEL_ADMIN'):
            try:
                SQL().del_admin_from_user_table(args[1])
                API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'DEL_ADMIN'))
                Log.log_info(get_value_by_key('LOG', 'DEL_ADMIN').format(user_id, args[1]))
            except Exception as e:
                Log.log_crit(e)

        # Команда удаления пользователя ИЗ БД (!!!)
        elif args[0] == get_value_by_key('ADMIN_COMMANDS', 'ADMIN_REM_USER'):
            try:
                SQL().del_row_from_user_table(args[1])
                API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'REM_ADMIN'))
                Log.log_info(get_value_by_key('LOG', 'REM_ADMIN').format(user_id, args[1]))
            except Exception as e:
                Log.log_crit(e)

        else: 
             API.messages_send(user_id, get_value_by_key('ADMIN_RESPONSE', 'UNKNOWN'))

    @staticmethod
    def in_user_table(user_id):
        SQL().insert_into_users_if_not_exists(user_id)




