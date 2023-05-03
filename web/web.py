from fastapi import FastAPI
from celery import Celery
# import dotenv
import os

app = FastAPI()


# dotenv.load_dotenv()

broker = os.getenv('ACELERY_BROKER')
backend = os.getenv('ACELERY_BACKEND')

print(broker, backend)
celery_app = Celery('hello', broker=broker, backend=backend)


@app.get("/hello")
def hello():
    result = celery_app.send_task('hello.task')
    print(result)
    return {"status": "hello"}