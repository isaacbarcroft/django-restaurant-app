# Generated by Django 3.2.8 on 2021-10-12 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0003_menuitem_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='description',
            new_name='desc',
        ),
    ]