from django.shortcuts import render
from django.http import HttpResponse
import time
from core.celery import app


@app.task
def my_task():
    time.sleep(10)
    open('test.txt', 'w').close()


def home(request):
    print(my_task)
    my_task.delay()
    return HttpResponse('Hello')
