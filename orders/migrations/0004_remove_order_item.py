# Generated by Django 3.2.8 on 2021-10-12 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_name_order_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
    ]
