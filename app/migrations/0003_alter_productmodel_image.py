# Generated by Django 4.2.4 on 2023-08-28 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products-images/'),
        ),
    ]
