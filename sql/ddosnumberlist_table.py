from sql.models import DdosNumberList
from sql.operations import commit, rollback


def add_number(user_id, number: str) -> bool:
    """
        Adds a number to the table if user_id is exists in users table\n
        Return True if added, or False if not
        """
    try:
        DdosNumberList.create(user_id=user_id,
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
        for user_bl in DdosNumberList.select().where((DdosNumberList.user_id == user_id) &
                                                     (DdosNumberList.number == number.lower().strip('+'))):
            user_bl.delete_instance()
            i += 1
        commit()
        if i == 0:
            return False
        return True
    except Exception:
        rollback()
        return False


def get_ddosnumberlist(isUnique: bool = True) -> dict or None:
    """
    Return the list of blacklist table {id : number}
    """
    try:
        numberList = DdosNumberList.select()
        if isUnique:
            res = dict()
            for row in numberList: res[f"{row.user_id}"] = row.number
        else:
            res = [f"{row.user_id} {row.number}" for row in numberList]
        commit()
        return res
    except Exception:
        rollback()
        return None
