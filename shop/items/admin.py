from django.contrib import admin
from items.models import Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name_slug', 'desc', 'is_sale', 'old_sale', 'is_active', 'curent_sale', 'name', 'image_tag', 'is_top', 'category']