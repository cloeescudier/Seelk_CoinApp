from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoinApp.settings')
app = Celery('CoinApp')

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')