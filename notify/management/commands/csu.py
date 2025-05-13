from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Creates a superuser if one does not exist'

    def handle(self, *args, **options):
        username = os.getenv('SUPERUSER_USERNAME', 'admin')
        email = os.getenv('SUPERUSER_EMAIL', 'admin@example.com')
        password = os.getenv('SUPERUSER_PASSWORD', 'adminpassword')

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists'))
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully'))
