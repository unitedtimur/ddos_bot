from src import config
from src.api import *
from src.sql import SQL


class Admin_Process:
    def __init__(self, sql: SQL):
        self.sql = sql

    def process(self, user_id, message):
        args = message.split()
        if len(args) < 2:
            messages_send(user_id, "Неверно переданы аргументы. Попробуйте снова.")
            return

        # If arg is {list}
        if args[1] == config.admin_command_args[0]:
            users = self.sql.get_rows_from_table('users')
            info = [get_fullname_by_user_id(user[0]) + ' id: ' + str(user[0]) + ' level: ' + user[1] for user in users]
            messages_send(user_id, '\n'.join(info))

            

