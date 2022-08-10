from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = 'Parse Privatbank archive rates'  # noqa: A003, VNE003

    def handle(self, *args, **options):
        pass