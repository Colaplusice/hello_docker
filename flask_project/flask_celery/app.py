from flask import Flask, Response
from celery import Celery


app = Flask(__name__)


def make_celery(app):
    celery = Celery(
        "app",
        backend=app.config["CELERY_RESULT_BACKEND"],
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


class Config:
    REDIS_HOST = "redis"
    REDIS_HOST = "127.0.0.1"
    REDIS_DB = 0
    REDIS_PORT = 6379

    REDLOCK_TIMEOUT = 10
    REDLOCK_BLOCKING_TIMEOUT = 5

    # celery
    from datetime import timedelta

    # redis 作为消息队列
    # CELERY_ACCEPT_CONTENT = ['pickle']
    # CELERY_TASK_SERIALIZER = 'pickle'
    # CELERY_RESULT_SERIALIZER = 'pickle'
    CELERY_BROKER_URL = "redis://redis:6379/0"
    # BROKER_URL = 'amqp://user:newpass@localhost:5672//'
    CELERY_TASK_PROTOCOL = 1
    # result_backend = 'redis://localhost:6379/1'
    CELERY_RESULT_BACKEND = "redis://redis:6379/1"
    CELERY_ACCEPT_CONTENT = ["json"]
    CELERYBEAT_SCHEDULE = {
        "add_beat": {
            "task": "app.test_beat",
            "schedule": timedelta(seconds=1),
            "args": (14, 14),
        }
    }


app.config.from_object(Config)
celery_app = make_celery(app)


@celery_app.task
def test_beat(a, b):
    print("this is a +b")


@celery_app.task
def work_1(a, b):
    print("this is beat")


@app.route("/")
def test_celery():
    work_1.delay(32, 32)
    return Response(200)


if __name__ == "__main__":
    app.run(debug=True)
