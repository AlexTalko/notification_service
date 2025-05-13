from django.urls import path
from notify.views import NotifyView

# Маршруты приложения notify
urlpatterns = [
    path('api/notify/', NotifyView.as_view(), name='notify'),  # Эндпоинт для отправки уведомлений
]
