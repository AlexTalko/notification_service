from django.contrib import admin
from .models import Notification, NotificationLog


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'message_preview', 'recipient', 'created_at', 'delay_display')
    list_filter = ('created_at', 'delay')
    search_fields = ('message', 'recipient')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)

    def message_preview(self, obj):
        return obj.message[:50] + ('...' if len(obj.message) > 50 else '')

    message_preview.short_description = 'Сообщение'

    def delay_display(self, obj):
        return obj.get_delay_display()

    delay_display.short_description = 'Задержка'


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'notification_message', 'notification_recipient', 'status', 'sent_at')
    list_filter = ('status', 'sent_at')
    search_fields = ('notification__message', 'notification__recipient', 'status', 'error_message')
    date_hierarchy = 'sent_at'
    readonly_fields = ('sent_at', 'error_message')
    list_select_related = ('notification',)

    def notification_message(self, obj):
        return obj.notification.message[:50] + ('...' if len(obj.notification.message) > 50 else '')

    notification_message.short_description = 'Уведомление'

    def notification_recipient(self, obj):
        return obj.notification.recipient

    notification_recipient.short_description = 'Получатель'
