#!/usr/bin/env python3
"""Jobs scheduling to be executed in the future"""
from jobs.sleep import sleep
from datetime import datetime, timedelta
import time

# schedule create job
eta = datetime.now() + timedelta(seconds=30)
job = sleep.apply_async(args=(10,), eta=eta)

# and sleep for 30 seconds
print(job.id, job.status)  # PENDING
time.sleep(30)

# 30 seconds later, sleep for another 10
print(job.id, job.status)  # PENDING
time.sleep(10)

# 10 seconds later, finally
print(job.id, job.status)  # SUCCESS
