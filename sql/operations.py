import sql.models


def commit():
    sql.models.db.commit()


def rollback():
    sql.models.db.rollback()
