from django.shortcuts import render
from items.models import Item


def index(r):
    items = Item.objects.all()
    return render(r, 'index.html', {'items': items})


def catalog(r):
    items = Item.objects.all()
    return render(r, 'catalog.html', {'items': items})
# Create your views here.


def category1(r):
    items = Item.objects.all()
    items_list = []
    for i in items:
        if i.category == '1':
            items_list.append(i)
    return render(r, 'category.html', {'items': items_list})


def category2(r):
    items = Item.objects.all()
    items_list = []
    for i in items:
        if i.category == '2':
            items_list.append(i)
    return render(r, 'category.html', {'items': items_list, 'categoru': 'category 2'})


def category3(r):
    items = Item.objects.all()
    items_list = []
    for i in items:
        if i.category == '3':
            items_list.append(i)
    return render(r, 'category.html', {'items': items_list, 'categoru': 'category 3'})


def category4(r):
    items = Item.objects.all()
    items_list = []
    for i in items:
        if i.category == '4':
            items_list.append(i)
    return render(r, 'category.html', {'items': items_list, 'categoru': 'category 4'})


def category5(r):
    items = Item.objects.all()
    items_list = []
    for i in items:
        if i.category == '5':
            items_list.append(i)
    return render(r, 'category.html', {'items': items_list, 'categoru': 'category 5'})


def item_detail(r, slug):
    item = Item.objects.get(name_slug=slug)
    return render(r, 'item_detail.html', {'item': item})

