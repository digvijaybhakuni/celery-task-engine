from celery import Celery
import time
import os

broker = str(os.getenv('ACELERY_BROKER'))
backend = str(os.getenv('ACELERY_BACKEND'))

print(broker, backend)

app = Celery('t1', broker=broker, backend=backend)

@app.task(name="hello.task")
def hello():
    print('hello tasks')
    time.sleep(10)
    return 'hello world'