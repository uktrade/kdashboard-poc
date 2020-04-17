from django.core.management.base import BaseCommand
from core.helpers import get_dashboards


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Getting dashboards')
        get_dashboards()
