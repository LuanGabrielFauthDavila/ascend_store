# Generated by Django 3.2.9 on 2022-01-28 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220128_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercadopagonotification',
            name='action',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='mercadopagonotification',
            name='api_version',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='mercadopagonotification',
            name='application_id',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='mercadopagonotification',
            name='date_created',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='mercadopagonotification',
            name='id_notification',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='mercadopagonotification',
            name='id_topic',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='mercadopagonotification',
            name='live_mode',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='mercadopagonotification',
            name='topic',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='mercadopagonotification',
            name='type',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='mercadopagonotification',
            name='user_id',
            field=models.CharField(blank=True, default='0', max_length=255),
        ),
    ]
