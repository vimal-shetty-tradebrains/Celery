from time import sleep
from celery import shared_task

@shared_task(name="Addition task")
def add(x,y):
    sleep(20)
    return x+y

@shared_task
def sub(x,y):
    sleep(10)
    return x-y



# Clear cache - Periodic task
@shared_task
def clear(id):
    print(f"cleared {id}")
    return id