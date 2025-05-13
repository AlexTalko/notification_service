from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from pydantic import ValidationError
from notify.validators import NotifyRequest
from notify.models import Notification
from notify.tasks import send_notification
from datetime import timedelta


# API-представление для обработки запросов на отправку уведомлений
class NotifyView(APIView):
    def post(self, request):
        try:
            # Валидация входящих данных с помощью Pydantic
            data = NotifyRequest(**request.data)
        except ValidationError as e:
            # Возврат ошибки при некорректных данных
            return JsonResponse({'error': e.errors()}, status=status.HTTP_400_BAD_REQUEST)

        # Преобразование получателя в список, если это строка
        recipients = [data.recipient] if isinstance(data.recipient, str) else data.recipient
        notifications = []

        # Сохранение уведомлений в базу данных
        for recipient in recipients:
            notification = Notification.objects.create(
                message=data.message,
                recipient=recipient,
                delay=data.delay
            )
            notifications.append(notification)

        # Планирование задач с учётом задержки
        for notification in notifications:
            delay_seconds = 0
            if data.delay == 1:
                delay_seconds = 3600  # 1 час
            elif data.delay == 2:
                delay_seconds = 86400  # 1 день

            # Запуск Celery-задачи с указанной задержкой
            send_notification.apply_async(
                args=[notification.id],
                countdown=delay_seconds
            )

        # Ответ об успешной постановке в очередь
        return JsonResponse({'status': 'Уведомления поставлены в очередь'}, status=status.HTTP_202_ACCEPTED)
