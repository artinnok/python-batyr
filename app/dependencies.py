from peewee import *
from environs import Env
from redis import Redis
from rq import Queue


environment = Env()
environment.read_env()

DATABASE_NAME = environment("DATABASE_NAME")
DATABASE_URL = environment("DATABASE_URL")

REDIS_URL = environment("REDIS_URL")


def get_db():
    """
    Соединяется с базой данных
    """

    db = PostgresqlDatabase(
        database=DATABASE_NAME,
        dsn=DATABASE_URL,
    )
    db.connect()

    return db


def get_queue():
    """
    возвращает очередь задач
    """

    redis = Redis.from_url(url=REDIS_URL)
    queue = Queue(connection=redis)

    return queue
