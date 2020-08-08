from peewee import *

db = PostgresqlDatabase("bot-test", user='postgres', password="masterkey", host="localhost", port=5433)


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = PrimaryKeyField(null=False)
    name = CharField(max_length=50, null=False)
    surname = CharField(max_length=50, null=False)
    privilege = CharField(max_length=20, null=False)

    class Meta:
        db_table = "users"
        order_by = ("user_id",)


class BlackList(BaseModel):
    user_id = ForeignKeyField(Users, related_name="fk_user_id", to_field="user_id", on_delete="cascade", null=False)
    number = CharField(20, null=False)

    class Meta:
        db_table = "black_list"
        order_by = ("user_id",)


class DdosNumberList(BaseModel):
    user_id = IntegerField(null=False)
    number = CharField(20, null=False)

    class Meta:
        db_table = "ddos_number_list"
        order_bt = ("user_id",)
