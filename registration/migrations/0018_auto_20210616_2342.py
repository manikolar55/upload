# Generated by Django 3.1.7 on 2021-06-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_auto_20210616_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='country_name',
            name='ThreeCharCountryCode',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country_name',
            name='TwoCharCountryCode',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
