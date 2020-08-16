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


def del_user(user_id) -> bool:
    """
    Remove user from users table and will removed all numbers from blacklist table\n
    Return True if removed or False if not
    """
    try:
        Users.get(user_id=user_id).delete_instance()
        # user = Users.get(user_id=user_id)
        # user.delete_instance()
        commit()
        return True
    except Exception:
        rollback()
        return False


def get_users() -> list:
    """
    Return the list of users {id : name : surname : privilege}
    """
    try:
        users = Users.select()
        res = []

        if users:
            res = [{
                'user_id': user.user_id,
                'name': user.name,
                'surname': user.surname,
                'privilege': user.privilege
            } for user in users]
            commit()

        return res
    except Exception:
        rollback()
        return []


def get_user(user_id) -> dict:
    """
    Return an user from users table with by user_id
    """
    try:
        user = Users.select().where(Users.user_id == user_id)
        res = {}

        if user:
            commit()
            res = {'user_id': user.user_id,
                   'name': user.name,
                   'surname': user.surname,
                   'privilege': user.privilege}

        return res
    except Exception:
        rollback()
        return {}


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


def update_info(user_id, name: str = None, surname: str = None, privilege: str = None) -> bool:

    data = {}
    if name:
        data[Users.name] = name
    if surname:
        data[Users.surname] = surname
    if privilege:
        data[Users.privilege] = privilege

    try:
        if Users.update(data).where(Users.user_id == user_id).execute():
            commit()
            return True

        return False
    except Exception:
        rollback()
        return False
