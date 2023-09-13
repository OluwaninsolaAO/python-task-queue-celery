# Python Task Queue with Celery

Exploring Task Queue with Celery, a Python Library.

### What is Task Queue

Task queues are used as a mechanism to distribute work across threads or machines.

A task queue’s input is a unit of work called a task. Dedicated worker processes constantly monitor task queues for new work to perform.

Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task the client adds a message to the queue, the broker then delivers that message to a worker.

A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.

Celery is written in Python, but the protocol can be implemented in any language. In addition to Python there’s node-celery and node-celery-ts for Node.js, and a PHP client.

Language interoperability can also be achieved exposing an HTTP endpoint and having a task that requests it (webhooks).

### Installing dependencies

A list of dependencies required for this project has been included in the `requirements.txt` file, this project also makes use of `redis` as the message broker and `sqlite` as the backend storage. These options can be configured or changed from the `celeryconfig.py` file at the project root.

```bash
$ sudo apt install redis-cli
$ pip install -r requirements.txt
```

### Start the queue server

Before you run any of the `*main.py` scripts, ensure the server is running else all jobs created will stay in `PENDING` state until the queue server is started.

```bash
$ celery -A queue_service worker --loglevel=info
```
