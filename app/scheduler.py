from time import sleep

import schedule

from tasks import hello_world
from dependencies import get_queue


def enqueue_task():
    queue = get_queue()
    queue.enqueue(hello_world)


if __name__ == "__main__":
    while True:
        schedule.run_pending()
        sleep(1)
