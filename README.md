# Python Task Queue with Celery

Exploring Task Queue with Celery, a Python Library.

### What is Task Queue

Task queues are used as a mechanism to distribute work across threads or machines.

A task queue’s input is a unit of work called a task. Dedicated worker processes constantly monitor task queues for new work to perform.

Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task the client adds a message to the queue, the broker then delivers that message to a worker.

A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.

Celery is written in Python, but the protocol can be implemented in any language. In addition to Python there’s node-celery and node-celery-ts for Node.js, and a PHP client.

Language interoperability can also be achieved exposing an HTTP endpoint and having a task that requests it (webhooks).
