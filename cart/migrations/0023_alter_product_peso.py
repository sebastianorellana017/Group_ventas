# Generated by Django 3.2.3 on 2021-07-09 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0022_alter_product_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='peso',
            field=models.IntegerField(default=0, null=True),
        ),
    ]