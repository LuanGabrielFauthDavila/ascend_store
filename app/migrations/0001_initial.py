# Generated by Django 3.2.9 on 2021-11-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pedido_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('usuario', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='produto_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='app/static/public/product_images/')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=55)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='shop_car_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('id_produto', models.IntegerField()),
            ],
        ),
    ]