# Generated by Django 4.2.5 on 2023-09-14 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_item_data_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='data_added',
        ),
    ]