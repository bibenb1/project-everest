# Generated by Django 3.1.4 on 2020-12-08 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20201208_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.sensor', to_field='identifier'),
        ),
    ]
