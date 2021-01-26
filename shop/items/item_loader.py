from items.models import Item
from shop.settings import DATA_DIR
from os import listdir
from os.path import isfile, join, isdir
import yaml
from django.core.files import File


class ItemLoader(object):

    def __init__(self, *args, **kwargs):
        self.dir = args[0]

    def process(self):
        self.get_item_or_create()
        self.save_meta_item()

    def get_item_or_create(self):
        try:
            self.item = Item.objects.get(name_slug=self.dir)
        except:
            self.item = Item()
            self.item.name_slug = self.dir
            self.item.save()

    def save_meta_item(self):
        path = DATA_DIR+'/'+self.dir+'/meta.yml'
        print('Saving meta for %s' % self.item.name_slug)
        meta = self.get_meta(path)
        self.item.name = meta['title']
        self.item.desc = meta['desc']
        self.item.is_active = meta['is_active']
        self.item.is_sale = meta['is_sale']
        self.item.old_sale = meta['old_sale']
        self.item.curent_sale = meta['curent_sale']
        self.item.is_top = meta['is_top']
        self.item.category = meta['category']
        self.item.save()
        try:
            im_path = DATA_DIR + '/' + self.dir + '/image.png'
            print('Loading image %s' % im_path)
            with open(im_path, 'rb') as img_file:
                self.item.image.save('image.png', File(img_file), save=True)
        except Exception as e:
            print(str(e))

    def get_meta(self, path):
        if isfile(path):
            f = open(path, 'r')
            str = f.read()
            f.close()
            yml = yaml.load(str, Loader=yaml.FullLoader)
            return yml
        else:
            return False

    @staticmethod
    def get_active_item_dirs():
        out = []
        onlydirs = [f for f in listdir(DATA_DIR) if isdir(join(DATA_DIR, f))]
        for d in onlydirs:
            if d.find('.') == -1:
                out.append(d)
        return out
