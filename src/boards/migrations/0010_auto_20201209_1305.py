# Generated by Django 3.1.4 on 2020-12-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0009_auto_20201209_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='date_received',
            field=models.DateTimeField(null=True),
        ),
    ]