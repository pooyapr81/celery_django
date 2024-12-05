# USE CELERY WITH REDIS IN DJANGO

Celery is an asynchronous task queue/job queue that is commonly used in web applications to handle time-consuming tasks in the background. It allows the main application (e.g., a web app) to remain responsive while tasks like sending emails, processing large datasets, or performing scheduled operations are executed in the background.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install celery.

```bash
pip install celery
```

## Usage
use the package with import that in celery.py
```python
from celery import Celery
```
after that use this code for using celery for task
```python
from core.celery import app
@app.task
#def my_task():
#   time.sleep(10)
#  open('test.txt', 'w').close()
```
also you can write tour task in tasks.py 

To get Redis recognized by celery, we write the following code at settings.py:
```python
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_DEFAULT_QUEUE = 'default'
```
then run the redis and type this in terminal:
```bash
 SET DJANGO_SETTINGS_MODULE=core.settings
```
```bash
 pip install celery[redis]
```
```bash
 celery -A core worker --pool=solo --loglevel=info
```
to create and run worker.

