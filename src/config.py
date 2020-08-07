from enum import Enum

levels = ["user", "vip", "admin"]

admin_command = "/admin"
admin_command_args = ["list", "set_level"]

general_command_args = { "ddos": "ddos", "add_w": "add_w" }

vip_command = "/vip"
user_command = "/user"

class GenCommands(ENUM):
    INFO = 1,
    DDOS = 2,
    BL = 3,

    def toGenCommands(str):

general_command_args = {""}

'''
/info
/ddos
/bl

/ddos
=====================
-t -> time
-n -> phone number
-th -> threads
=====================
/bl
=====================
-add
-del
=====================
/info
=====================
-h -> help
-bl -> black list
-ddos -> phone numbers being under ddos
'''
