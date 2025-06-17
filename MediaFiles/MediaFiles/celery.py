import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MediaFiles.settings')

app = Celery('MediaFiles')

# Load task modules from all registered Django app configs
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'log-every-5-minutes': {
        'task': 'media_app.tasks.log_to_file',
        'schedule': crontab(minute='*/5'),  # every 5 minutes
    },
}
app.conf.worker_pool = 'solo'
