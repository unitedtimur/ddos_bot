import copy

class Level:
    CONFIG = {
        "ddos_time_limit": 100,
        "ddos_threads": 20,
        "ddos_multi_threads": 1,
        "ddos_count_of_numbers": 1
    }

class Admin_Level(Level):
    def __init__(self):
        self.CONFIG = copy.deepcopy(super(Admin_Level, self).CONFIG)

class User_Level(Level):
    def __init__(self):
        self.CONFIG = copy.deepcopy(super(User_Level, self).CONFIG)
