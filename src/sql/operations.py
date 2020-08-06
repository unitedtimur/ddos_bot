import peewee
from src.sql.models import *


def init_database_connection():
    try:
        db.connect()
        Users.create_table()
        BlackList.create_table()
        print("Database has been initialized...")
        print("Users and black_list tables has been initialized...")
    except peewee.InternalError as px:
        db.rollback()
        print(str(px))


def commit():
    db.commit()


def rollback():
    db.rollback()


def add_user(user_id, name, surname, privilege) -> bool:
    """
    Adds a user to the table if it doesn't exist\n
    Return True if added, or False if not
    """
    try:
        Users.create(user_id=user_id,
                     name=name.lower().strip(),
                     surname=surname,
                     privilege=privilege.lower().strip())
        commit()
        return True
    except Exception:
        db.rollback()
        return False


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
        db.rollback()
        return False


def rem_number(user_id, number) -> bool:
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

def get_users() -> list:
    """
    Return the list of users {id : name : surname : privilege}
    """
    try:
        users = Users.select()
        res = [f"{user.user_id} {user.name} {user.surname} {user.privilege}" for user in users]
        return res
        commit()
    except Exception:
        rollback()
        return False

def get_blacklist(isUnique: bool = True) -> dict:
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
        return res
        commit()
    except Exception:
        rollback()
        return False