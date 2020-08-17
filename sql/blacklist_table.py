from sql.models import BlackList
from sql.operations import commit, rollback


def add_number(user_id, number) -> bool:
    """
    Adds a number to the table if user_id is exists in users table\n
    Return True if added, or False if not
    """
    try:
        BlackList.create(user_id=user_id, number=number)
        commit()
        return True

    except Exception:
        rollback()
        return False


def del_number(user_id, number: str) -> bool:
    """
    Remove number from blacklist table\n
    Return True if removed or False if not
    """
    try:
        numbers = BlackList.select().where((BlackList.user_id == user_id) & (BlackList.number == number))
        if numbers:
            for user_bl in numbers:
                user_bl.delete_instance()
            commit()
            return True

        return False
    except Exception:
        rollback()
        return False


def get_blacklist(isUnique: bool = True) -> dict:
    """
    Return the list of blacklist table {id : number}
    """
    try:
        users_bl = None
        res = {}

        if isUnique:
            users_bl = BlackList.select()
        else:
            users_bl = BlackList.select().distinct(BlackList.user_id)

        for user_bl in users_bl:
            res[user_bl.user_id] = user_bl.number

        commit()
        return res
    except Exception:
        rollback()
        return {}


def get_numbers(user_id) -> list:
    """
    Return a number or numbers
    """
    try:
        numbers = BlackList.select().where(BlackList.user_id == user_id)
        res = []

        if numbers:
            res = [{'user_id': number.user_id, 'number': number.number} for number in numbers]
            commit()

        return res
    except Exception:
        rollback()
        return []

def is_in_bl(number: str) -> bool:

    try:
        bl_numbers = BlackList.select(BlackList.number)

        if bl_numbers:
            commit()
            for bl_number in bl_numbers:
                if number == bl_number.number:
                    return True

        return False
    except Exception:
        rollback()
        return False
