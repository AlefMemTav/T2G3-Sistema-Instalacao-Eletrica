# Generated by Django 4.2 on 2024-04-17 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0019_delete_atmosfericdischargesystem'),
        ('systems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtmosfericDischargeSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atmosferic_discharge_systems', to='places.place')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atmosferic_discharge_systems', to='places.room')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atmosferic_discharge_systems', to='systems.system')),
            ],
            options={
                'db_table': 'atmosferic_discharge_system',
            },
        ),
    ]
