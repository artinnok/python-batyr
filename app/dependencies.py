from peewee import *
from environs import Env


environment = Env()
environment.read_env()

DATABASE_NAME = environment("DATABASE_NAME")
DATABASE_URI = environment("DATABASE_URL")


def get_db():
    """
    Соединяется с базой данных
    """

    db = PostgresqlDatabase(
        database=DATABASE_NAME,
        dsn=DATABASE_URI,
    )
    db.connect()

    return db
