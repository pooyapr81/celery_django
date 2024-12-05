from celery import shared_task
from core.celery import app
@app_task
def my_task_2():
    file = open('test.txt', 'a')
    file.write('hello world ')
    file.close()