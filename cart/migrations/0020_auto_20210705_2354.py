# Generated by Django 3.2.3 on 2021-07-06 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0019_auto_20210705_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='colour',
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_colours',
        ),
    ]
