# Generated by Django 3.1.5 on 2021-01-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_sale',
            field=models.BooleanField(default=False, verbose_name='is sale'),
        ),
    ]
