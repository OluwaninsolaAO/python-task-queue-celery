#!/usr/bin/env python3
"""Simple usage Celery Queue"""

from jobs.sleep import sleep
import time

job_list = []


def job_status(job_list: list = [], i=None):
    """Print Jobs List Status"""
    time.sleep(i/5)
    status = [job.status for job in job_list]
    print('>>> Total Jobs = {}'.format(len(job_list)))
    for x in set(status):
        print('>>> {} = {}'.format(x, status.count(x)))


for i in range(25):
    print('>>> sleep.delay({})'.format(i))
    job = sleep.delay(i)
    job_list.append(job)
    job_status(job_list=job_list, i=i)

print('All jobs sent, waiting for the last job to complete')
print('All done, last job: {}'.format(job.get()))
