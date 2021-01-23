from django.db import models
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from django.urls import reverse
from os import listdir
from os.path import isfile, join, isdir
import markdown
import os

# Create your models here.
def parse_md(txt):
    try:
        txt = txt.decode('UTF-8')
    except:
        pass
    return mark_safe(markdown.markdown(txt,extensions=['extra', 'smarty'], output_format='html5'))


class Item(models.Model):
    CHOICES = (
        ('1', '1 category'),
        ('2', '2 category'),
        ('3', '3 category'),
        ('4', '4 category'),
        ('5', '5 category'),
    )

    name = models.CharField(max_length=250, verbose_name=_(u'Name'), blank=True, null = True)
    desc = models.TextField(verbose_name=_(u'Description'), blank=True, null = True)
    image = models.ImageField(verbose_name=_(u'Image'), upload_to='item_images', blank=True, null=True)
    name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True, null = True)
    is_active = models.BooleanField(verbose_name=_('Is published?'), default=False)
    is_sale = models.BooleanField(verbose_name=_('is sale'), default=False)
    curent_sale = models.CharField(max_length=150, blank=True, verbose_name=_(u'curent_sale'))
    old_sale = models.CharField(max_length=150, blank=True, verbose_name=_(u'old_sale'))
    is_top = models.BooleanField(verbose_name=_('is top'), default=False)
    category = models.CharField(verbose_name=_('category'), max_length=300, choices=CHOICES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'slug': self.name })


    @property
    def image_tag(self):
        return mark_safe('<img width="60" src="%s" />' % self.image.url)