from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.conf.broker_connection_retry_on_startup = True
app.config_from_object('django.conf:settings', namespace='CELERY')

# type this in terminal:
# SET DJANGO_SETTINGS_MODULE=core.settings
# pip install celery[redis]
# celery -A core worker --pool=solo --loglevel=info
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'my_task_in_every_2_sec': {
        'task': 'home.tasks.my_task_2',
        'schedule': 2,
    },
}
# celery -A core beat
