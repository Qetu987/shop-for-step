from django.shortcuts import render
from items.models import Item


def index(r):
    items = Item.objects.all()
    return render(r, 'index.html', {'items': items})


def catalog(r):
    items = Item.objects.all()
    return render(r, 'catalog.html', {'items': items})
# Create your views here.
