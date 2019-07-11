from celery import Celery
broker_url = 'sqs://notValidKey:notValidSecret@localhost:9324'
broker_transport_options = {'queue_name_prefix': 'celery-'}
app = Celery('tasks', broker=broker_url)


@app.task
def add(x, y):
    return x + y
