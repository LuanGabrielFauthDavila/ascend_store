# Generated by Django 3.2.9 on 2021-11-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211114_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_car_model',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]