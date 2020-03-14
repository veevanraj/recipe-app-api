import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """To pause execution until data base is availabele"""

    def handle(self, *args, **options):
        self.stdout.write("waiting for database response...")
        db_conn =None
        while  not db_conn:
            try :
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable waiting  1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
