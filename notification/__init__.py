# Импорт Celery приложения для его доступности
from .celery import app as celery_app

# Экспорт Celery приложения
__all__ = ('celery_app',)
