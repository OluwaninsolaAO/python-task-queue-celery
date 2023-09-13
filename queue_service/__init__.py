#!/usr/bin/env python3
"""A simple Celery Task Queue Service"""
from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

import jobs.sleep  # noqa
