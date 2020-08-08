from sql.models import Users, db
from sql.operations import commit, rollback


def add_user(user_id, name, surname, privilege) -> bool:
    """
    Adds a user to the table if it doesn't exist\n
    Return True if added, or False if not
    """
    try:
        Users.create(user_id=user_id,
                     name=name,
                     surname=surname,
                     privilege=privilege.lower().strip())
        commit()
        return True
    except Exception:
        db.rollback()
        return False


def rem_user(user_id) -> bool:
    """
    Remove user from users table and will removed all numbers from blacklist table\n
    Return True if removed or False if not
    """
    try:
        user = Users.get(user_id=user_id)
        user.delete_instance()
        commit()
        return True
    except Exception:
        rollback()
        return False


def get_users() -> list or None:
    """
    Return the list of users {id : name : surname : privilege}
    """
    try:
        users = Users.select()
        res = [f"{user.user_id} {user.name} {user.surname} {user.privilege}" for user in users]
        commit()
        return res
    except Exception:
        rollback()
        return None


def get_user(user_id) -> str or None:
    """
    Return an user from users table with by user_id
    """
    try:
        user = Users.select().where(Users.user_id == user_id)[0]
        commit()
        return f"{user.user_id} {user.name} {user.surname} {user.privilege}"
    except Exception:
        rollback()
        return None

def get_privilege(user_id) -> str or None:
    """
    Return the privilege from users table by user_id
    """
    try:
        user = Users.select().where(Users.user_id == user_id)[0]
        commit()
        return str(user.privilege)
    except Exception:
        rollback()
        return None
