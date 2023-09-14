#!/usr/bin/env python3
"""A simple Job Definition for sleep"""
import time
from queue_service import app


@app.task
def sleep(n: int) -> str:
    """Using time.sleep(n) as delay and returning a str response"""
    time.sleep(n)
    return 'sleep(for {n} seconds)'.format(n=n)


@app.task(bind=True, max_retries=3)
def fail(self, n: int):
    """Delibrate failure and then resolve after 3 retries"""
    time.sleep(n)
    try:
        if self.request.retries != 3:
            raise Exception('You shall not pass!')
    except Exception as exc:
        print('Task failed, retrying in {n} seconds'.format(n=n))
        self.retry(exc=exc, countdown=n)
    return 'Fly you fools!'
