# Generated by Django 3.2.8 on 2021-10-28 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0006_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
