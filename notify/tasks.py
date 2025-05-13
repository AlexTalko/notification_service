from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from telegram import Bot
from notify.models import Notification, NotificationLog
import asyncio


# Celery-задача для отправки уведомления
@shared_task
def send_notification(notification_id: int):
    try:
        # Получение уведомления из базы данных
        notification = Notification.objects.get(id=notification_id)
        recipient = notification.recipient
        message = notification.message

        # Отправка email, если получатель — email
        if '@' in recipient:
            send_mail(
                subject='Уведомление',
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient],
                fail_silently=False,
            )
            status = 'success'
            error_message = None
        # Отправка в Telegram, если получатель — Telegram ID
        else:
            bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
            asyncio.run(bot.send_message(chat_id=recipient, text=message))
            status = 'success'
            error_message = None

    except Exception as e:
        # Обработка ошибок при отправке
        status = 'failed'
        error_message = str(e)

    # Сохранение лога отправки
    NotificationLog.objects.create(
        notification=notification,
        status=status,
        error_message=error_message
    )
