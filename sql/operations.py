import ddos_bot.sql.models


def commit():
    ddos_bot.sql.models.db.commit()


def rollback():
    ddos_bot.sql.models.db.rollback()
