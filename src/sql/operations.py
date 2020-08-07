from src.sql.models import db


def commit():
    db.commit()


def rollback():
    db.rollback()
