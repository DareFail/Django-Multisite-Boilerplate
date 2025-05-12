import os
from celery import Celery
from celery.signals import task_failure
from django.core.mail import mail_admins

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

app = Celery("main")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()

@task_failure.connect
def celery_task_error_email_handler(sender=None, task_id=None, exception=None, args=None, kwargs=None,
                                   traceback=None, einfo=None, **kw):
    subject = f"[Celery] Error in task {sender.name}: {exception}"
    message = (
        f"Task Name: {sender.name}\n"
        f"Task ID: {task_id}\n"
        f"Args: {args}\n"
        f"Kwargs: {kwargs}\n"
        f"Exception: {exception}\n"
        f"Traceback:\n{einfo.traceback}"
    )
    mail_admins(subject, message)
