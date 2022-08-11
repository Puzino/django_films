from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Parse Privatbank archive rates'  # noqa: A003, VNE003

    def handle(self, *args, **options):
        pass
