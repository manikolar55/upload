# Generated by Django 3.1.7 on 2021-04-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_server_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server_products',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
