# Generated by Django 3.2.9 on 2021-11-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_produto_model_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido_model',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido_model',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='produto_model',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto_model',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto_model',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shop_car_model',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop_car_model',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='produto_model',
            name='file',
            field=models.FileField(upload_to='app/static/public/product_images/'),
        ),
    ]
