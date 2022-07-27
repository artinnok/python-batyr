from datetime import datetime

from rq_scheduler import Scheduler

from dependencies import get_redis
from tasks import hello_world


RUN_INTERVAL = 30


def create_schedule():
    """
    создать расписание
    """

    redis = get_redis()
    scheduler = Scheduler(connection=redis)

    scheduler.schedule(
        scheduled_time=datetime.utcnow(),
        func=hello_world,
        interval=RUN_INTERVAL,
    )
