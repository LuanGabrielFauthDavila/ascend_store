# Generated by Django 3.2.9 on 2022-01-30 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20220129_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcar',
            name='pedido',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='app.pedido', verbose_name='Pedido'),
            preserve_default=False,
        ),
    ]
