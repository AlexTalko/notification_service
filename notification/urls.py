from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Сервис уведомлений'
admin.site.site_title = 'Админка уведомлений'
admin.site.index_title = 'Управление рассылками'

# Главные маршруты проекта
urlpatterns = [
    path('admin/', admin.site.urls),  # Админ-панель
    path('', include('notify.urls')),  # Подключение маршрутов приложения notify
]
