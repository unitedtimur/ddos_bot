from enum import Enum

from src import config
from src.admin_process import Admin_Process
from src.user_process import User_Process


class Level(Enum):
    USER = "user"
    VIP = "vip"
    ADMIN = "admin"
    UNKNOWN = "unknown"

class Process:
    def __init__(self):
        self.sql = None
        self.admin_process = Admin_Process(self.sql)
        self.user_process = User_Process(self.sql)

    def process(self, user_id, message):
        id = user_id
        msg = message.lower()
        level = self.get_level(id)

        # If user is admin
        if level == "admin":
            self.admin_process.process(id, msg)
            print(f"Admin request from {id}")
        # If user
        elif level == "user":
            self.user_process.process(id, msg)
            print(f"User requst from {id}")
        # If user is vip
        elif level == "vip_1":
            print(f"Vip request from {id}")
        else:
            print("Unknown command")

    # Check user level
    def get_level(self, user_id):
        user = self.sql.get_user_from_users(user_id)
        if not user: return "unknown"
        return user[1]

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