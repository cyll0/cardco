# Generated by Django 4.2.5 on 2023-09-14 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_item_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='date_added',
        ),
    ]
