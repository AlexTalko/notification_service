# Notification Service 📬

**Notification Service** — сервис для отправки уведомлений по email и Telegram через REST API. Поддерживает асинхронную
обработку задач и админ-панель для управления рассылками и логами.

---

## Технологический стек 🛠️

- **Python 3.12**
- **Django 4.2.7** + **Django REST Framework**
- **PostgreSQL 15+** — база данных
- **Redis 7+** — брокер для Celery
- **Celery 5.3.6** — асинхронные задачи
- **python-dotenv** — управление `.env`
- **python-telegram-bot** — Telegram API

---

## Запуск и тестирование 🚀

### Установка

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/AlexTalko/notification_service.git
   cd notification_service
   ```

2. Создайте виртуальное окружение:
    ```bash 
    python -m venv .venv 
    source .venv/bin/activate  # macOS/Linux
    .venv\Scripts\activate  # Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4. Создайте .env в корне проекта и заполните согласно *.env.sample* в корне репозитория:
    ```bash
    touch .env
    ```
5. Настройте PostgreSQL:
    ```bash
    psql -U postgres
    ```
    ```bash
    CREATE DATABASE notification_service;
    ```

## Запуск проекта

1. **Примените миграции:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
2. **Создайте суперпользователя (для тестирования через админ панель):**
    ```bash
    python manage.py csu
    ```

### Запустите сервисы:

1. Redis-сервер:
    ```bash
    redis-server
    ```
2. Django-сервер:
    ```bash
    python manage.py runserver
    ```
3. Celery (в отдельном терминале):
    ```bash
    celery -A notification worker --loglevel=info
    ```

## Тестирование

### API:

   ```bash
    curl -X POST http://localhost:8000/api/notify/ \
    -H "Content-Type: application/json" \
    -d '{

      "message": "Тест email",
      "recipient": "your-email@example.com",
      "delay": 0
      }'
   ```   

   ```bash
    curl -X POST http://localhost:8000/api/notify/ \
    -H "Content-Type: application/json" \
    -d '{
     "message": "Тест Telegram",
     "recipient": "123456789",
     "delay": 0
     }'  
   ```

**Проверьте email (входящие/спам) и Telegram (чат с ботом).**

**Админка:**

Откройте http://localhost:8000/admin/ (логин: admin, пароль: adminpassword по умолчанию).

Просматривайте уведомления (Notifications) и логи (Notification logs).

Добавляйте уведомления вручную.





