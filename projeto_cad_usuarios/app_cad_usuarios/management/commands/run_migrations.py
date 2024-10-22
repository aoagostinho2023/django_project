from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run migrations'

    def handle(self, *args, **kwargs):
        self.stdout.write('Running makemigrations...')
        call_command('makemigrations')
        self.stdout.write('Running migrate...')
        call_command('migrate')
        self.stdout.write('Migrations complete.')