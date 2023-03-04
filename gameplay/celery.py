import os
from django.conf import settings
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gameplay.settings')

app = Celery('project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_joke_3s':{
        'task':'app.tasks.add',
        'schedule':12.0,
        'options': {
            'expires': 13.0,
        },
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()