from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(email=settings.SUPERUSER_EMAIL).exists():
            User.objects.create_superuser(
                email=settings.SUPERUSER_EMAIL,
                nickname=settings.SUPERUSER_NICKNAME,
                password=settings.SUPERUSER_PASSWORD,
            )