# Generated by Django 4.2.4 on 2023-08-26 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='products_order', to='app.productmodel'),
        ),
    ]