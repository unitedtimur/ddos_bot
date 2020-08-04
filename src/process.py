from enum import Enum

from src import config
from src.admin_process import Admin_Process
from src.sql import SQL


class Level(Enum):
    USER = "user"
    VIP = "vip"
    ADMIN = "admin"
    UNKNOWN = "unknown"

class Process:
    def __init__(self):
        self.sql = SQL()
        self.admin_process = Admin_Process(self.sql)

    def process(self, user_id, message):
        command = self.what_command(message)
        # If user is admin and entered admin command
        if self.is_level(user_id, 'admin') and command == Level.ADMIN:
            self.admin_process.process(user_id, message)
            print(f"Admin request from {user_id}")
        # If user or admin and entered user command
        elif (self.is_level(user_id, 'user') or self.is_level(user_id, 'admin')) and command == Level.USER:
            print(f"User request from {user_id}")
        else:
            print("Unknown command")

    # Check user level
    def is_level(self, user_id, level: str):
        user = self.sql.get_user_from_users(user_id)
        if not user: return False
        if user[1] == level: return True
        return False

    # Check entered command
    def what_command(self, message) -> Level:
        command = message.split()[0]
        if command == config.user_command:
            return Level.USER
        elif command == config.admin_command:
            return Level.ADMIN
        elif command == config.vip_command:
            return Level.VIP
        else:
            return Level.UNKNOWN