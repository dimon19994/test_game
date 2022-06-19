from flask_login import UserMixin
from peewee import CharField, ForeignKeyField

from models import _Model


class User(UserMixin, _Model):
    class Meta:
        db_table = "users"

    username = CharField(unique=True, max_length=255)
    password = CharField(max_length=255)


class Token(_Model):
    class Meta:
        db_table = "tokens"

    token = CharField(primary_key=True)
    user_id = ForeignKeyField(User)
