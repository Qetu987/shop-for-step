from django.core.management.base import BaseCommand, CommandError
from items.models import Item
from shop.settings import DATA_DIR
from items.item_loader import ItemLoader


class Command(BaseCommand):
  
    def handle(self, *args, **options):
        print('Start item %s' %DATA_DIR)
        for d in ItemLoader.get_active_item_dirs():
            print(d)
            item = ItemLoader(d)
            item.process()