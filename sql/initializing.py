import peewee
from ddos_bot.sql.models import *
from ddos_bot.sql.operations import *


def init_database_connection():
    try:
        db.connect()
        Users.create_table()
        BlackList.create_table()
        DdosNumberList.create_table()
        print("Database has been initialized...")
        print("Tables has been initialized...")
        commit()
    except peewee.InternalError as px:
        rollback()
        print(str(px))