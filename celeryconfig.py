# Celery Config

broker_url = 'redis://localhost:6379/0'
result_backend = 'db+sqlite:///db.sqlite'
broker_connection_retry_on_startup = True
worker_concurrency = 10
task_publish_retry = True
