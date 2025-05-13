from django.db import models


# Модель для хранения уведомлений
class Notification(models.Model):
    message = models.CharField(max_length=1024)  # Текст сообщения (макс. 1024 символа)
    recipient = models.CharField(max_length=150)  # Получатель (email или Telegram ID)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    delay = models.PositiveSmallIntegerField(
        choices=((0, 'Без задержки'), (1, '1 час'), (2, '1 день')))  # Задержка отправки

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    def __str__(self):
        return f"Уведомление для {self.recipient}"


# Модель для логирования попыток отправки
class NotificationLog(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE,
                                     related_name='logs')  # Связь с уведомлением
    status = models.CharField(max_length=50)  # Статус отправки (успех/ошибка)
    sent_at = models.DateTimeField(auto_now_add=True)  # Время попытки
    error_message = models.TextField(blank=True, null=True)  # Сообщение об ошибке (если есть)

    class Meta:
        verbose_name = 'Лог уведомления'
        verbose_name_plural = 'Логи уведомлений'

    def __str__(self):
        return f"Лог для {self.notification}"
