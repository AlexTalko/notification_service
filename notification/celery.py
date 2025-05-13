import os
from celery import Celery

# Установка переменной окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification.settings')

# Инициализация Celery
app = Celery('notification')
# Загрузка настроек Celery из Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')
# Автоматическое обнаружение задач
app.autodiscover_tasks()
