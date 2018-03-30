from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from raven.contrib.django.raven_compat.models import client

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kargs):
        try:
            2 / 0
        except ZeroDivisionError:
            client.captureException()
