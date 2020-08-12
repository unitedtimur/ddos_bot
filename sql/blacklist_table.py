from sql.models import BlackList
from sql.operations import commit, rollback


def add_number(user_id, number) -> bool:
    """
    Adds a number to the table if user_id is exists in users table\n
    Return True if added, or False if not
    """
    try:
        BlackList.create(user_id=user_id,
                         number=number.lower().strip('+'))
        commit()
        return True
    except Exception:
        rollback()
        return False


def rem_number(user_id, number: str) -> bool:
    """
    Remove number from blacklist table\n
    Return True if removed or False if not
    """
    try:
        i = 0
        for user_bl in BlackList.select().where((BlackList.user_id == user_id) &
                                                (BlackList.number == number.lower().strip('+'))):
            user_bl.delete_instance()
            i += 1
        commit()
        if i == 0:
            return False
        return True
    except Exception:
        rollback()
        return False


def get_blacklist(isUnique: bool = True) -> dict or None:
    """
    Return the list of blacklist table {id : number}
    """
    try:
        users_bl = BlackList.select()
        if isUnique:
            res = dict()
            for row in users_bl: res[f"{row.user_id}"] = row.number
        else:
            res = [f"{row.user_id} {row.number}" for row in users_bl]
        commit()
        return res
    except Exception:
        rollback()
        return None


def get_number(user_id):
    """
    Return a number or numbers
    """
    try:
        numbers = BlackList.select().where(BlackList.user_id == user_id)
        res = [f"{number.user_id} {number.number}" for number in numbers]
        commit()
        return res
    except Exception:
        rollback()
        return list()

def get_numbers() -> list:
    """
    Return list of numbers
    """
    try:
        numbers = BlackList.select()
        list = []
        for num in numbers: list.append(num.number)
        return list
        commit()
    except Exception:
        rollback()