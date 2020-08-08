from settings import config


class Permission:
    def __init__(self, user_status: str):
        self.status = user_status
        self.max_ddos_time = config.standard_limits['dtime']
        self.max_attacks_per_day = config.standard_limits['atks']
        self.max_bl_numbers = config.standard_limits['bl']
        self.available_commands = config.available_commands[user_status]


