# Generated by Django 3.2.8 on 2021-10-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
    ]
