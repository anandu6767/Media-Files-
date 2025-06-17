from celery import shared_task
from datetime import datetime
import os
from django.conf import settings

@shared_task
def log_to_file():
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_line = f"{timestamp} Scheduled task ran.\n"

    log_path = os.path.join(settings.BASE_DIR, "task_log.txt")
    with open(log_path, "a") as f:
        f.write(log_line)
