from src import config
from src.api import messages_send
from src.sql.models import SQL


class User_Process:
    def __init__(self, sql: SQL):
        self.sql = sql

    def process(self, user_id, message):
        args = message.split()
        if len(args) < 2:
            messages_send(user_id, "Неверно переданы аргументы. Попробуйте снова.")
            return

        # If args is { ddos (number) (time) }
        if args[0] != config.user_command:
            pass
