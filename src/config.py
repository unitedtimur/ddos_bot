from enum import Enum

levels = ["user", "vip", "admin"]

admin_command = "/admin"
admin_command_args = ["list", "set_level"]

general_command_args = { "ddos": "ddos", "add_w": "add_w" }

vip_command = "/vip"
user_command = "/user"

HelpMessage = '''
/ddos -- команда для ddos
=====================
-t  число -- время атаки в секундах
-th число -- количество потоков
-n  номер -- номер телефона
=====================
/bl -- команда для списка номеров, запрещенных для ddos
=====================
-add номер -- добавить номер телефона в список
-del номер -- удалить номер телефона из списка
=====================
/info -- информативная команда
=====================
-h    -- информация о доступных командах
-bl   -- показать номера в списке
-ddos -- показать номера, находящиеся под ddos
=====================
'''

class PrivilageLvl(ENUM):
    ADMIN = 1,
    USER = 2,
    VIP = 3,
    UNKNOWN = 4

    def toPrivLvl(plevel: str):
        plevel = plevel.lower()

        if plevel == 'admin':
            return ADMIN
        elif plevel == 'user':
            return USER
        elif plevel == 'vip':
            return VIP
        else:
            return UNKNOWN

class GenCommands(ENUM):
    INFO = 1,
    DDOS = 2,
    BL = 3,
    UNKNOWN = 4

    def toGenCommands(pcommand: str):
        pcommand = pcommand.lower()
        pcommand = pcommand.replace('/', '').replace('\\', '')

        if pcommand == 'info':
            return INFO
        elif pcommand == 'ddos':
            return DDOS
        elif pcommand == 'bl':
            return BL
        else:
            return UNKNOWN

class SubCommands(ENUM):
    TIME = 1,
    PNUM = 2,
    THREAD = 3,
    ADD = 4,
    DEL = 5,
    HELP = 6,
    BL = 7,
    DDOS = 8,
    UNKNOWWN = 9

    def toSubCommands(pcommand: str):
        pcommand = pcommand.lower()
        pcommand = pcommand.replace('-', '')

        if pcommand == 't':
            return TIME
        elif pcommand == 'n':
            return PNUM
        elif pcommand == 'th':
            return THREAD
        elif pcommand == 'add':
            return ADD
        elif pcommand == 'del':
            return DEL
        elif pcommand == 'h':
            return HELP
        elif pcommand == 'bl':
            return BL
        elif pcommand == 'ddos':
            return DDOS
        else:
            return UNKNOWN
