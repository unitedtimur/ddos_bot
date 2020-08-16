import sql.users_table as utable
import settings.config as config


class Passport:

    def __init__(self, user_id):
        self.user_id = user_id
        self.privilege = utable.get_privilege(user_id)
        self.commands_config = config.commands_config[self.privilege]
