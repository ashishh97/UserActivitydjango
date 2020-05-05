from django.core.management.base import BaseCommand
from custom_app.factories import ActivityPeriodFactory
class Command(BaseCommand):
    help = 'Populates the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=20,
            type=int,
            help='The number of fake activity to create.')

    def handle(self, *args, **options):
        for _ in range(options['users']):
            ActivityPeriodFactory.create()
        