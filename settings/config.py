from enum import Enum

levels = ["user", "vip", "admin"]

admin_command = "/admin"
admin_command_args = ["list", "set_level"]

general_command_args = { "ddos": "ddos", "add_w": "add_w" }

vip_command = "/vip"
user_command = "/user"

available_commands = {
    'admin' : {
        '/ddos' : {
            '-t'  : ('time', 1, float('inf')),
            '-th' : ('threads', 1, float('inf')),
            '-n'  : ('number', 1, -1)
        },
        '/bl'   : {
            '-add' : ('command', 1, -1),
            '-del' : ('command', 1, -1)
        },
        '/info' : {
            '-h'    : ('command', 0),
            '-bl'   : ('command', 0),
            '-ddos' : ('command', 0)
        }
    },
    'vip'   : {
        '/ddos': {
            '-t': ('time', 1, 3600),
            '-th': ('threads', 1, 100),
            '-n': ('number', 1, -1)
        },
        '/bl': {
            '-add': ('command', 1, -1),
            '-del': ('command', 1, -1)
        },
        '/info': {
            '-h': ('command', 0),
            '-bl': ('command', 0),
            '-ddos': ('command', 0)
        }
    },
    'user'  : {
        '/ddos' : {
            '-t'  : ('time', 1, 150),
            '-n'  : ('number', 1, -1)
        },
        '/info' : {
            '-h'    : ('command', 0),
            '-ddos' : ('command', 0)
        }
    }
}

standard_limits = {
    'dtime': 40, #макс ддос время в секундах
    'th'   : 15, #макс потоков
    'atks' : 3,  #макс атак в день
    'bl'   : 2   #макс номеров в черном списке
}

HelpMessage = '''
/ddos -- команда для ddos
=====================
-t  число -- время атаки в секундах
-th число -- количество потоков
-n  номер -- номер телефона
=====================
/bl -- команда для списка номеров, запрещенных для ddos
=====================
-l
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