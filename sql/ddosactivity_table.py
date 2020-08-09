from sql.models import DdosActivity
from sql.operations import *


def add_number(user_id, number: str) -> bool:
    """
        Adds a number to the table\n
        Return True if added, or False if not
        """
    try:
        DdosActivity.create(user_id=user_id,
                            number=number.lower().strip('+'))
        commit()
        return True
    except Exception:
        rollback()
        return False


def rem_number(user_id, number: str) -> bool:
    """
    Remove number from ddos_number_list table\n
    Return True if removed or False if not
    """
    try:
        i = 0
        for user_bl in DdosActivity.select().where((DdosActivity.user_id == user_id) &
                                                   (DdosActivity.number == number.lower().strip('+'))):
            user_bl.delete_instance()
            i += 1
        commit()
        if i == 0:
            return False
        return True
    except Exception:
        rollback()
        return False
