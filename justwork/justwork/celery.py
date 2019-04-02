from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'justwork.settings')

app = Celery('justwork')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True, default_retry_delay=300, max_retries=5)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))