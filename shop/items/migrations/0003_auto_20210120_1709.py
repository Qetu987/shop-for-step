# Generated by Django 3.1.5 on 2021-01-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20210120_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='item',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sale',
        ),
        migrations.AddField(
            model_name='item',
            name='curent_sale',
            field=models.CharField(blank=True, max_length=150, verbose_name='curent_sale'),
        ),
        migrations.AddField(
            model_name='item',
            name='old_sale',
            field=models.CharField(blank=True, max_length=150, verbose_name='old_sale'),
        ),
    ]
