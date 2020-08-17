from sql.models import DdosNumberList
from sql.operations import commit, rollback
from datetime import datetime


def add_number(user_id, number: str) -> bool:
    """
        Adds a number to the table if user_id is exists in users table\n
        Return True if added, or False if not
        """
    try:
        if DdosNumberList.insert(user_id=user_id,
                                 number=number,
                                 date=datetime.today().strftime('%Y-%m-%d')):
            commit()
            return True

        return False
    except Exception:
        rollback()
        return False


def del_number(user_id, number: str) -> bool:
    """
    Remove number from ddos_number_list table\n
    Return True if removed or False if not
    """
    try:
        numbers = DdosNumberList.select().where((DdosNumberList.user_id == user_id) &
                                                (DdosNumberList.number == number))
        if numbers:
            for user_bl in numbers:
                user_bl.delete_instance()
            commit()
            return True

        return False
    except Exception:
        rollback()
        return False


def get_ddosnumberlist(isUnique: bool = True) -> dict:
    """
    Return the list of blacklist table {id : number}
    """
    try:
        users_bl = None
        res = {}

        if isUnique:
            users_bl = DdosNumberList.select()
        else:
            users_bl = DdosNumberList.select().distinct(DdosNumberList.user_id)

        for user_bl in users_bl:
            res[user_bl.user_id] = {'number': user_bl.number, 'date': user_bl.date}

        commit()
        return res
    except Exception:
        rollback()
        return {}


def get_committed_attacks(user_id, date: str) -> list:
    try:

        attacks = DdosNumberList.select().where((DdosNumberList.user_id == user_id) &
                                                (DdosNumberList.date == date))
        res = []

        if attacks:
            res = [{'user_id': attack.user_id,
                    'number': attack.number,
                    'date': attack.date
                    } for attack in attacks]

        return res
    except Exception:
        rollback()
        return []
