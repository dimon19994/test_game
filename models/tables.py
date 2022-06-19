from flask_login import UserMixin
from peewee import CharField, ForeignKeyField, IntegerField

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


class Room(_Model):
    class Meta:
        db_table = "rooms"

    name = CharField()
    max_players = IntegerField()
    players_count = IntegerField()
    creator = ForeignKeyField(User)


class UsersInRoom(_Model):
    class Meta:
        db_table = "users_in_room"

    user_id = ForeignKeyField(User)
    room_id = ForeignKeyField(Room)