# Generated by Django 3.1.4 on 2020-12-08 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_remove_sensordata_proximity'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProximityData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.sensordata')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_device', to='boards.sensor')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_device', to='boards.sensor')),
            ],
            options={
                'unique_together': {('batch', 'target')},
            },
        ),
    ]