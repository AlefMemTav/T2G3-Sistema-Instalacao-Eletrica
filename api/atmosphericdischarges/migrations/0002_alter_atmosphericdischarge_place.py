# Generated by Django 4.2 on 2024-04-23 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0021_room_place_room_systems'),
        ('atmosphericdischarges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmosphericdischarge',
            name='place',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atmospheric_discharges', to='places.place'),
        ),
    ]