from functools import wraps

from peewee import Model, datetime as peewee_datetime
from playhouse.postgres_ext import PostgresqlExtDatabase

from config import DB_CONFIG

peewee_now = peewee_datetime.datetime.now

db = PostgresqlExtDatabase(**DB_CONFIG)
db.commit_select = True
db.autorollback = True


def open_db_connection():
    if db.is_closed():
        db.connect()


def close_db_connection():
    if not db.is_closed():
        db.close()


def db_connect_wrapper(func):
    """
    connect to db and disconnect from it

    """

    @wraps(func)
    def wrapper(*args, **kwds):
        try:
            open_db_connection()
            return func(*args, **kwds)
        finally:
            close_db_connection()

    return wrapper


class _Model(Model):
    class Meta:
        database = db

    def __repr__(self):
        return "{class_name}(id={id})".format(class_name=self.__class__.__name__, id=self.id)

    @classmethod
    def get_by_id(cls, id):
        try:
            return cls.get(cls.id == id)
        except cls.DoesNotExist:
            return None
